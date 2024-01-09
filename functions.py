import aiohttp
from aiogram import Bot

async def is_port_open(url, port):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}:{port}"):
                return True
    except:
        return False

async def is_service_running(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url):
                return True
    except:
        return False

async def is_http_200_ok(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status == 200
    except:
        return False

async def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)