from pyrogram import Client, Filters


@Client.on_message(Filters.private & Filters.text)
async def _(client, message):
    print(message.text)
