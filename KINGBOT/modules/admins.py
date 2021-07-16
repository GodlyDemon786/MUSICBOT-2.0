

from asyncio.queues import QueueEmpty
from KINGBOT.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from KINGBOT.function.admins import set
from KINGBOT.helpers.channelmusic import get_chat_id
from KINGBOT.helpers.decorators import authorized_users_only, errors
from KINGBOT.helpers.filters import command, other_filters
from KINGBOT.services.callsmusic import callsmusic


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("**🏆 Admin cache refreshed!**")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("**🙅 Nothing is playing boss!**")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("**▶️ Paused successfully!!**")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("** 🤷 Nothing is paused boss!**")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("**⏸ Resumed successfully!!**")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**🤔❗ Nothing is streaming or may be last song!!**")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("**😌 Stopped streaming!!**")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**😅 Nothing is playing to skip or may be it last song !**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- ♀️♂️Skipped **{skip[0]}**\n- Now Playing **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")
