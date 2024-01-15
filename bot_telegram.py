import sys
sys.path.append('.')
from functions import is_port_open, is_service_running, is_http_200_ok, send_telegram_message
import asyncio
import os

async def monitor_website(url, interval, bot_token, chat_id):
    try:
        while True:
            service_running = await is_service_running(url)
            port_open = await is_port_open(url, 80)
            http_200_ok = await is_http_200_ok(url)

            if not port_open:
                await send_telegram_message(bot_token, chat_id, f"El puerto 80 de {url} está cerrado o no responde.")
                break
            elif not service_running:
                await send_telegram_message(bot_token, chat_id, f"El puerto responde pero el servicio web en {url} no está funcionando.")
                break
            elif not http_200_ok:
                await send_telegram_message(bot_token, chat_id, f"El servicio web en {url} está devolviendo un código de estado HTTP que no es 200.")
                break

            await asyncio.sleep(interval)


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
