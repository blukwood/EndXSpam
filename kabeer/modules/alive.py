# (C) 2021, Jayant Kageri

from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters, Client
from kabeer import app1, app2, CMD_HELP, StartTime
from sys import version_info
from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message


CMD_HELP.update(
    {
        "Alive": """
**Alive**
  `alive` -> For Checking Pyrogram Alive Status
  `ping` -> For Pinging Pyrogram
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@app1.on_message(filters.command("alive", PREFIX))
@app2.on_message(filters.command("alive", PREFIX))
async def alive(_, m):
    uptime = get_readable_time((time.time() - StartTime))
    msg = "I am Alive"
    await Client.send_message(message.chat.id, msg, disable_web_page_preview=True)


@app1.on_message(filters.command("ping", PREFIX))
@app2.on_message(filters.command("ping", PREFIX))
async def pingme(_, message: Message):
    app_info = await Client.get_me()
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await Client.send_message(message.chat.id, f"**Pong** : `{m_s} ms`", disable_web_page_preview=True)
