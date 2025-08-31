import os
import aio_pika

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://kalo:kalo@amqp/")

class RabbitMQConnection:
    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        if self.connection and not self.connection.is_closed:
            return self.channel

        self.connection = await aio_pika.connect_robust(RABBITMQ_URL)
        self.channel = await self.connection.channel()
        return self.channel

    async def get_exchange(self, exchange_name: str):
        channel = await self.connect()
        return await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.DIRECT, durable=True)

    async def get_queue(self, queue_name: str):
        channel = await self.connect()
        return await channel.declare_queue(queue_name, durable=True)
