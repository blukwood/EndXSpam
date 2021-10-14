from pyrogram.types import *
from kabeer import *
from pyrogram import *
from config import *
from os import *

@app1.on_message(filters.command("json", PREFIX))
@app2.on_message(filters.command("json", PREFIX))
async def start(client, message):
    try:
        if message.reply_to_message:
            msg = message.reply_to_message
        else:
            msg = message

        if len(str(msg_info)) > int("4096"):
            file = open("json.txt", "w+")
            file.write(str(msg_info))
            file.close()
            await app.send_document(
                message.chat.id,
                "json.txt",
                caption="Returned JSon",

            )
            remove("json.txt")

        else:
            await message.edit(str(msg_info))

    except Exception as e:
        await message.edit(f"{e}")
