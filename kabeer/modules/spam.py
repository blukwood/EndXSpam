from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from kabeer import app1, app2, CMD_HELP

import asyncio


@app1.on_message(filters.command('delspam', PREFIX))
@app2.on_message(filters.command('delspam', PREFIX))
async def statspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@app1.on_message(filters.command('spam', PREFIX))
@app2.on_message(filters.command("spam", PREFIX))
async def spam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


        
@app1.on_message(filters.command('bspam', PREFIX))
@app2.on_message(filters.command("bspam", PREFIX))
async def fastspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.02)
        return
    
    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.02)


@app1.on_message(filters.command('sspam', PREFIX))
@app2.on_message(filters.command("sspam", PREFIX))
async def slowspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)


CMD_HELP.update(
    {
        "spam": """
**spam**
  `spam` -> spam
"""
    }
)

