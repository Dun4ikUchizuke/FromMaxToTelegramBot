from create_bot import bot
from aiogram import F, Router
from aiogram.types import URLInputFile
from os import getenv
import requests



router = Router()
user_chat_id = int(getenv('USER_CHAT_ID'))
max_chat_id = getenv('MAX_CHAT_ID')
greenApiInstID = getenv('idInstance')
greenApiTokenInst = getenv('apiTokenInstance')

async def GetMessages():
    url = f"""https://3100.api.green-api.com/v3/waInstance{greenApiInstID}/lastIncomingMessages/{greenApiTokenInst}?minutes=1"""
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    for currentObj in range(len(data)-1, -1, -1):
        if data[currentObj]['chatId'] == max_chat_id:
            match(data[currentObj]['typeMessage']):
                case 'textMessage' | 'extendedTextMessage':
                    await bot.send_message(chat_id=user_chat_id, text=data[currentObj]['textMessage'])
                    continue
                case 'extendedTextMessage':
                    await bot.send_message(chat_id=user_chat_id, text=data[currentObj]['textMessage'])
                    continue
                case 'imageMessage':
                    image = URLInputFile(data[currentObj]['downloadUrl'])
                    await bot.send_photo(chat_id=user_chat_id, photo=image, caption=data[currentObj]['caption'])
                    continue
                case 'videoMessage':
                    video = URLInputFile(data[currentObj]['downloadUrl'])
                    await bot.send_video(chat_id=user_chat_id, video=video, caption=data[currentObj]['caption'])
                    continue
                case 'documentMessage':
                    doc = URLInputFile(data[currentObj]['downloadUrl'])
                    await bot.send_document(chat_id=user_chat_id, document=doc, caption=data[currentObj]['caption'])
                    continue
                case 'audioMessage':
                    audio = URLInputFile(data[currentObj]['downloadUrl'])
                    await bot.send_audio(chat_id=user_chat_id, audio=audio, caption=data[currentObj]['caption'])
                    continue
                case _:
                    continue
    data = None
