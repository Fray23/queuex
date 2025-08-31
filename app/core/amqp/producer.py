import json
from aio_pika import Message, DeliveryMode
from app.core.amqp.connection import RabbitMQConnection


class TaskQueueProducer:
    def __init__(self, exchange_name="tasks"):
        self.exchange_name = exchange_name
        self.connection = RabbitMQConnection()

    async def publish_task(self, task_type: str, task_id: str):
        channel = await self.connection.connect()

        exchange = await channel.declare_exchange(self.exchange_name, durable=True, type="direct")

        await exchange.publish(
            Message(
                body=json.dumps({"task_id": task_id, "type": task_type}).encode(),
                delivery_mode=DeliveryMode.PERSISTENT,
            ),
            routing_key=task_type
        )
