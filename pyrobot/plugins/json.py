"""Get Detailed info about any message
Syntax: .json"""

from pyrogram import Client, Filters

import io
import os
import aiofiles

from pyrobot import MAX_MESSAGE_LENGTH, COMMAND_HAND_LER


@Client.on_message(Filters.command("json", COMMAND_HAND_LER)  & Filters.me)
async def jsonify(client, message):
    the_real_message = None
    reply_to_id =  None

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
        reply_to_id = message.message_id

    try:
        await client.send_message('me', the_real_message)
    except Exception as e:
        async with aiofiles.open("message.json", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        
        await client.send_document(
            chat_id='me',
            document="message.json",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        
        os.remove("json.text")
    
    await message.delete()
