from app.core.amqp.amqp_client import AmqpClient
from app.core.amqp.connection import RabbitMQConnection
from .handlers.resize_image import resize_image

EXCHANGE_NAME = "tasks"
QUEUE_NAME = "worker_queue"

conn = RabbitMQConnection()
amqp = AmqpClient(conn=conn, exchange_name=EXCHANGE_NAME, queue_name=QUEUE_NAME)

amqp.register_handler("resize-image", resize_image)
