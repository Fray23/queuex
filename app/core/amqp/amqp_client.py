import logging
from typing import Callable, Awaitable, Dict, Any

from aio_pika import IncomingMessage
from aio_pika.abc import AbstractIncomingMessage

from app.core.amqp.connection import RabbitMQConnection

logger = logging.getLogger(__name__)

Handler = Callable[[AbstractIncomingMessage], Awaitable[Dict[str, Any]]]


class AmqpClient:
    def __init__(self, conn: RabbitMQConnection, exchange_name: str, queue_name: str) -> None:
        self.conn = conn
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.handlers: Dict[str, Handler] = {}
        self.exchange = None
        self.queue = None

    def register_handler(self, routing_key: str, handler: Handler):
        self.handlers[routing_key] = handler

    async def _consumer_wrapper(self, routing_key: str, handler: Handler):
        async def _on_message(message: IncomingMessage):
            async with message.process(ignore_processed=True):
                try:
                    await handler(message)
                except Exception as e:
                    logger.exception("Handler error for %s: %s", routing_key, e)
        return _on_message

    async def setup(self):
        channel = await self.conn.connect()

        self.exchange = await self.conn.get_exchange(self.exchange_name)
        self.queue = await self.conn.get_queue(self.queue_name)

        for routing_key, handler in self.handlers.items():
            await self.queue.bind(self.exchange, routing_key=routing_key)
            await self.queue.consume(await self._consumer_wrapper(routing_key, handler))
            logger.info("Registered handler for routing_key=%s", routing_key)

    async def close(self):
        if self.conn.connection and not self.conn.connection.is_closed:
            await self.conn.connection.close()
