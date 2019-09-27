#!/bin/sh
# -*- coding: utf-8 -*-
# the entire source code is GPL, except this file,
# which is AGPL
# (c) 2017

# the below two lines were taken without
# permission from 
# https://github.com/friendly-telegram/friendly-telegram/blob/master/install.sh#L62
if [ "$OSTYPE" = "linux-android" ]; then
  pkg install -y python git || { echo "installation of Python and GiT failed"; exit 2; }
  # the above lines were taken without 
  # permission from 
  # https://github.com/friendly-telegram/friendly-telegram/blob/master/install.sh#L62
  # create a virtual environment
  python3.7 -m venv venv
  . ./venv/bin/activate
  mkdir -p /sdcard/Telegram
  # create and change into accessible sub directory
  cd /sdcard/Telegram
  # install async
  pip install https://github.com/pyrogram/pyrogram/archive/asyncio.zip
  git clone https://github.com/SpEcHiDe/PyroGramUserBot
  cd PyroGramUserBot
  # generate string session
  python3 GenerateStringSession.py
  cd ..
  # cleanup
  rm -rf PyroGramUserBot
fi
