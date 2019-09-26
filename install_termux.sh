#!/bin/sh
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

if [ "$OSTYPE" = "linux-android" ]; then
  pkg install -y python git || { echo "installation of Python and GiT failed"; exit 2; }
  python3.7 -m venv venv
  . ./venv/bin/activate
  mkdir -p /sdcard/Telegram
  cd /sdcard/Telegram
  pip install https://github.com/pyrogram/pyrogram/archive/asyncio.zip
  git clone https://github.com/SpEcHiDe/PyroGramUserBot
  cd PyroGramUserBot
  python3 GenerateStringSession.py
  cd ..
  rm -rf PyroGramUserBot
fi
