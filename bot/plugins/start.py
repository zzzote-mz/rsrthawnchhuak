from pyrogram import filters
from pyrogram.types import Message
from bot import JunctionBot


@JunctionBot.on_message(filters.command("start") & filters.incoming & filters.private)
async def _(c: JunctionBot, m: Message):
    await m.reply_text(
        "Hi {} Ka hming chu ZigZag ania. Automatic a chat forward thei Bot ka ni e,min siamtu hi @rsrmusic ani e",
        parse_mode="markdown",
        reply_to_message_id=m.message_id
    )
