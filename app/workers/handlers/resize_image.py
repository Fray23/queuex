import asyncio
import json
import logging
import os
from typing import Awaitable, Callable, Dict, Any
from aio_pika.abc import AbstractIncomingMessage


async def resize_image(message: AbstractIncomingMessage) -> dict:
    try:
        payload = json.loads(message.body.decode() or "{}")
        print("get message: ", payload)
    except Exception:
        payload = {}
    await asyncio.sleep(0.1)
