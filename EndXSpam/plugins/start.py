from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Updates", url="https://t.me/RhythmOfficial"
                    ),
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/RhythmOff"
                    )
                ]
            ]
        )
    )



