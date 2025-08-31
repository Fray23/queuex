import asyncio
from app.workers.amqp_entrypoint import amqp


async def main():
    try:
        await amqp.setup()
        await asyncio.Future()
    finally:
        await amqp.close()

if __name__ == "__main__":
    asyncio.run(main())
