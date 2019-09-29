"""Update profile pic automaticaly everry 60 seconds
Syntax: .autopic"""

from pyrogram import Client, Filters
from PIL import Image, ImageFont, ImageDraw 

import io
import os
import time
import traceback
import aiofiles

from pyrobot import MAX_MESSAGE_LENGTH, COMMAND_HAND_LER

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

UPDATE_PIC = True


@Client.on_message(Filters.command("autopic", COMMAND_HAND_LER)  & Filters.me)
async def autopic(client, message):
    logger.info()
    global UPDATE_PIC
    
    try:
        if UPDATE_PIC:
            UPDATE_PIC = False
            logger.info('profile updation stoped')
            return
        
        font = ImageFont.truetype("font.ttf", 70)
        
        while UPDATE_PIC:
            if int(time.time())%60 == 0:
                base_pic = "pics/base_profile_pic.jpg"
                
                new_pic = "pics/new_profile_pic.jpg"
                
                img = Image.open(base_pic)
                
                width, height = img.size
                
                draw = ImageDraw.Draw(img)
                
                tim = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(minutes=30, hours=5)))
                
                content = f"@odysseusmax\nDate: {tim.day}.{tim.month}.{tim.year}\nTime: {tim.hour}:{tim.minute}:{tim.second}\nUTC+5:30"
                
                draw.text((0, width), content,(255,255,255),font=font)
                
                img.save(new_pic)
                
                await client.set_profile_photo(new_pic)
                
                await aiofiles.os.remove(new_pic)
                
                logger.info(f'profile pic updated at {tim}')
    except Exception:
        logger.error(traceback.format_exc())
