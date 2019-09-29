"""Telegram Ping / Pong Speed
Syntax: .ping"""

from pyrogram import Client, Filters

from datetime import datetime

from pyrobot import COMMAND_HAND_LER


# -- Constants -- #
ALIVE = "`I'm here.`"
HELP = "Get lost"
REPO = ("Userbot is available on GitHub:\n"
        "https://github.com/odysseusmax/PyroGramUserBot")
# -- Constants End -- #


@Client.on_message(Filters.command("ping", COMMAND_HAND_LER)  & Filters.me)
async def ping(client, message):
    start_t = datetime.now()
    await message.edit("Pong!")
    end_t = datetime.now()
    time_taken_s = int((end_t - start_t).microseconds / 1000)
    await message.edit(f"Ping-Pong Speed\n`{time_taken_s}ms`")


@Client.on_message(Filters.command("repo", COMMAND_HAND_LER)  & Filters.me)
async def repo(client, message):
    await message.edit(REPO)


@Client.on_message(Filters.command("helpme", COMMAND_HAND_LER)  & Filters.me)
async def help_me(client, message):
    await message.edit(HELP)


@Client.on_message(Filters.command("alive", COMMAND_HAND_LER)  & Filters.me)
async def alive(client, message):
    await message.edit(ALIVE)
