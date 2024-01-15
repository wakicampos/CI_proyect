import sys
sys.path.append('.')
from functions import is_port_open, is_service_running, is_http_200_ok, send_telegram_message
import asyncio
import os

async def monitor_website(url, interval, bot_token, chat_id):
    try:
        while True:
            # Comprueba si el servicio está funcionando, el puerto está abierto y el estado HTTP es 200
            if await is_service_running(url) and await is_port_open(url, 80) and await is_http_200_ok(url):
                await send_telegram_message(bot_token, chat_id, f"Todo en orden con el servicio en {url}.")
            else:
                await send_telegram_message(bot_token, chat_id, f"Se detectó un problema en {url}.")
                break
            await asyncio.sleep(interval)l)

    except asyncio.CancelledError:
        await send_telegram_message(bot_token, chat_id, f"La tarea ha sido cancelada.")
    finally:
        await send_telegram_message(bot_token, chat_id, f"Cierre del bot...")

if __name__ == "__main__":
    url = "http://scanme.nmap.org/"
    interval = 10  # segundos
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    asyncio.run(monitor_website(url, interval, bot_token, chat_id))
