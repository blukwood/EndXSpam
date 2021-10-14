from config import PREFIX
import asyncio
from kabeer import LOGGER, app1, app2
from kabeer import CMD_HELP
from pyrogram import Client, filters
from pyrogram.types import Message


CMD_HELP.update(
    {
        "tagall": """
**Alive**
  `alive` -> For Checking Pyrogram Alive Status
  `ping` -> For Pinging Pyrogram
"""
    }
)


@app1.on_message(filters.command("alive", PREFIX))
@app2.on_message(filters.command("alive", PREFIX))
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    msg = "Hey, M Alive"
    await client.send_message(chat_id, text=msg)
