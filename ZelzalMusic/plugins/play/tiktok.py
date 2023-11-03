#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
import os
import requests
import aiohttp
import aiofiles

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from ZelzalMusic import app
from ZelzalMusic.plugins.play.filters import command

@app.on_message(command(["/tok", "تيك", "/tik"]))
async def tiktok_video(client, message):
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ التحميـل مـن تيـك تـوك . . .</b>")
    idd = message.from_user.id
    mc = message.chat.id
    url = "https://www.tikwm.com/api/?url={}".format(query)
    res = requests.get(url).json()
    video = res['data']['play']
    title = res['data']['title']
    share = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="- مشاركه .", url='https://t.me/share/url?url={}'.format(query))
        ]
    ])
    app.send_video(
        mc,
        video,
        caption='- {} .'.format(title),
        reply_markup=share,
        reply_to_message_id=message.message_id
    )
    await m.delete()
