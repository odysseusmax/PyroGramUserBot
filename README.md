# PyroGramUserBot 🔥🤖

A Telegram Userbot based on [Pyrogram](https://github.com/pyrogram/pyrogram)

## installing

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### The Legacy Way
Simply clone the repository and run the main file:

```bash
$ git clone https://github.com/odysseusmax/PyroGramUserBot

$ cd PyroGramUserBot

$ virtualenv venv

$ source venv/bin/activate

$ pip3 install -r requirements.txt

$ python3 -m pyrobot
```


## Getting config.py values

An example `config.py` file could be:

**Not All of the variables are mandatory**

__The UserBot should work by setting only these variables__

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 12345
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  HU_STRING_SESSION = "z25ONsATiAoufHuw3OxZuev0gGa84Jp2pHnDIbzp2DSVOi1mtgWLEzucFCYqYEKbHcfnt9qu9zhxIJkYZ6r8fr2ff3kQIoYbVFmIww6O7r9TiTirj_gMS2eOBRG1QlNuH5ZvInOjcXqe5OFeI7tutH8bHHNSvpA3BuCP6u_YAnGDcynwD7ajSx0iIeY4GcZMysK09PwOpJJdBkEH6xBaOSwHJg_SQLInftfajMJ8F2jzbMQ8NW4rfGKs8rZ9IeVowu2mXjUueeixXXTRmYg18Wjk7wbRL6WejLfB_gwA14MDsFMR5b1bFB9LYpN3iHSDCh2LLLJGkGfX6Y6j1SXB9nMDYRPsaaD
"
```

`HU_STRING_SESSION` can be generated by running `python3 GenerateStringSession.py` in any GNU/Linux system, with Python3 and the requirements installed.


## Credits, and Thanks to

* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
* [Colin Shark](https://telegram.dog/ColinShark) for his [PyroBot](https://git.colinshark.de/PyroBot/PyroBot)
