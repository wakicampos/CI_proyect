from functions import is_port_open, is_service_running, is_http_200_ok, send_telegram_message
import asyncio

async def monitor_website(url, interval, bot_token, chat_id):
    while True:
        if not await is_service_running(url):
            await send_telegram_message(bot_token, chat_id, f"El servicio web en {url} no está funcionando.")
            break
        elif not await is_port_open(url, 80):
            await send_telegram_message(bot_token, chat_id, f"El puerto 80 de {url} está cerrado o no responde.")
            break
        elif not await is_http_200_ok(url):
            await send_telegram_message(bot_token, chat_id, f"El servicio web en {url} está devolviendo un código de estado HTTP que no es 200.")
            break
        await asyncio.sleep(interval)
        
if __name__ == "__main__":
    url = "http://scanme.nmap.org"
    interval = 10 # segundos
    bot_token = "6573594161:AAG0EA0Awrt7CeL97-bDwOowNBsk4C8nRgc"
    chat_id = "1981377416"
    asyncio.run(monitor_website(url, interval, bot_token, chat_id))
