from config import PREFIX
import asyncio
from kabeer import LOGGER, app1, app2
from kabeer import CMD_HELP
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Voice
from helpers.callmusic import callsmusic

@app1.on_message(filters.command("alive", PREFIX))
@app2.on_message(filters.command("alive", PREFIX))
async def vcraid(client: Client, message: Message):
  lel = await message.reply("Please Wait....")
  audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
  if audio:
    file_name = get_file_name(audio)
    file_path = await convert(
      (await message.reply_to_message.download(file_name))
      if not path.isfile(path.join("downloads", file_name)) else file_name
    )
    else:
      return await lel.edit_text("Bsdk, Reply to Audio.")
    if message.chat.id in callsmusic.pytgcalls.active_calls:
      await message.reply("Already Playing")
      return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply("Playing...")
        return await lel.delete()
