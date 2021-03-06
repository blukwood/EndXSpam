import os
from importlib import import_module, reload
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers.handler import Handler
from kabeer import LOGGER, app1, app2
from config import PREFIX

@app1.on_message(filters.command("install", PREFIX))
async def load_plugin(client: Client, message: Message):
    status_message = await message.reply("...")
    try:
        if message.reply_to_message is not None:
            down_loaded_plugin_name = await message.reply_to_message.download(
                file_name="./kabeer/modules/"
            )
            if down_loaded_plugin_name is not None:
                # LOGGER.info(down_loaded_plugin_name)
                relative_path_for_dlpn = os.path.relpath(
                    down_loaded_plugin_name,
                    os.getcwd()
                )
                # LOGGER.info(relative_path_for_dlpn)
                lded_count = 0
                path = Path(relative_path_for_dlpn)
                module_path = ".".join(
                    path.parent.parts + (path.stem,)
                )
                # LOGGER.info(module_path)
                module = reload(import_module(module_path))
                # https://git.io/JvlNL
                for name in vars(module).keys():
                    # noinspection PyBroadException
                    try:
                        handler, group = getattr(module, name).handler

                        if isinstance(handler, Handler) and isinstance(group, int):
                            client.add_handler(handler, group)
                            LOGGER.info(
                                '[{}] [LOAD] {}("{}") in group {} from "{}"'.format(
                                    client.session_name,
                                    type(handler).__name__,
                                    name,
                                    group,
                                    module_path
                                )
                            )
                            lded_count += 1
                    except Exception:
                        pass
                await status_message.edit(
                    f"Installed {lded_count}"
                )
    except Exception as error:
        await status_message.edit(
            f"ERROR: <code>{error}</code>"
        )
