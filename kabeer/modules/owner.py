import asyncio
import time
import os

from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from kabeer import app1, app2, CMD_HELP
from config import PREFIX
# Help
CMD_HELP.update(
    {
        "Owner Tools": f"""
**Owner Stuff,**

   `block` - To Block a User
   `unblock` - To Unblock a Blocked User
   `chats` - To Count your Chats (Unstable due to Floodwait Limits)
"""
    }
)


# To Block a user
@app1.on_message(filters.command("block", PREFIX))
@app2.on_message(filters.command("block", PREFIX))
async def block_dumb(_, message: Message):
  shit_id = message.chat.id
  r_msg = message.reply_to_message
  try:
    if r_msg:
      await app.block_user(r_msg.from_user.id)
      await message.edit("`Successfully Blocked This User`")
    else:
      await app.block_user(shit_id)
      await message.edit("`Successfully Blocked This User`")
  except Exception as lol:
    await message.edit(f"**Error:** `{lol}`")

# To Unblock User That Already Blocked
@app2.on_message(filters.command("unblock", PREFIX))
@app1.on_message(filters.command("unblock", PREFIX))
async def unblock_boi(_, message: Message):
  good_bro = int(message.command[1])
  try:
    await app.unblock_user(good_bro)
    await message.edit(f"`Successfully Unblocked The User` \n**User ID:** `{good_bro}`")
  except Exception as lol:
    await message.edit(f"**Error:** `{lol}`")


# To Get How Many Chats that you are in (PM's also counted)
@app1.on_message(filters.command("chats", PREFIX))
@app2.on_message(filters.command("chats", PREFIX))
async def ubgetchats(_, message: Message):
  total=0
  async for dialog in app.iter_dialogs():
    try:
      await app.get_dialogs_count()
      total = total+1
      await message.edit(f"**Total Chats Counted:** `{total}`")
    except FloodWait as e:
      await time.sleep(e.x)
