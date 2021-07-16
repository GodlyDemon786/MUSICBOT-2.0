

from pyrogram import filters
from pyrogram.types import Message

from KINGBOT.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Hi there, This is a music assistant service .\n\n  🤔 Nothing is here:- \n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - It is 100% safe\n   - Any quary contact @KINGBOTOFFICIALCHAT\n 🤗🤗 REGARDS @KINGBOTOFFICIAL ⭐\n\n",
    )
    return
