from pyrogram import Client
from pytgcalls import PyTgCalls

from kabeer import app1, app2
from etc.services.queues import queues

pytgcalls = PyTgCalls(Client)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(chat_id, queues.get(chat_id)["file"])


run = pytgcalls.run
