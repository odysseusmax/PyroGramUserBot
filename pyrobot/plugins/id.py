"""Get ID of current chat
Syntax: .id"""

from pyrogram import Client, Filters

from pyrobot import COMMAND_HAND_LER


@Client.on_message(Filters.command("id", COMMAND_HAND_LER)  & Filters.me)
async def get_id(client, message):
    text = f"Chat ID: `{message.chat.id}`\nMessage ID: `{message.message_id}`\n"
    
    if message.reply_to_message:
        text += f"Replied Message ID: `{message.reply_to_message.message_id}`\nReplied message from User ID: `{message.reply_to_message.from_user.id}`"
    
    await message.edit_text(text)
