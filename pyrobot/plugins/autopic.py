"""Update profile pic automaticaly everry 60 seconds
Syntax: .autopic"""

from pyrogram import Client, Filters
from PIL import Image, ImageFont, ImageDraw 

import os
import time
import asyncio
import logging
import datetime
import traceback

from pyrobot import MAX_MESSAGE_LENGTH, COMMAND_HAND_LER

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

UPDATE_PIC = False


@Client.on_message(Filters.command("autopic", COMMAND_HAND_LER)  & Filters.me)
async def autopic(client, message):
    global UPDATE_PIC
    
    try:
        if UPDATE_PIC:
            UPDATE_PIC = False
            
            logger.info('stopping profile pic updation')
            
            await message.edit_text('stopping profile pic updation')
            
            return
        
        UPDATE_PIC = True
        
        font = ImageFont.truetype("font.ttf", 40)
        
        await message.edit_text('profile pic updation started')
        
        logger.info('profile pic updation started')
        
        while UPDATE_PIC:
            base_pic = "pics/base_profile_pic.jpg"
                
            new_pic = "pics/new_profile_pic.jpg"
                
            img = Image.open(base_pic)
                
            width, height = img.size
            
            draw = ImageDraw.Draw(img)
                
            tim = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(minutes=30, hours=5)))
                
            content = f"@odysseusmax\nDate: {tim.day}.{tim.month}.{tim.year}\nTime: {tim.hour}:{tim.minute}:{tim.second}\nUTC+5:30"
                
            draw.multiline_text(xy = (0, 300), text = content,
                                fill = (255,255,255), font=font,
                                align="center"
                            )
                
            img.save(new_pic)
                
            await client.set_profile_photo(new_pic)
                
            os.remove(new_pic)
                
            logger.info(f'profile pic updated at {tim}. Sleeping for 60s...')
            
            await asyncio.sleep(60)
        
        logger.info(f'profile pic updation stopped')
    except Exception:
        logger.error(traceback.format_exc())
