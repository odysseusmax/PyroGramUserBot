from pyrogram import Client, Filters


@Client.on_message(Filters.chat(777000))
async def _(client, message):
    print(message.text)
