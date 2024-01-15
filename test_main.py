import sys
sys.path.append('.')
from functions import is_port_open, is_service_running, is_http_200_ok, send_telegram_message
import pytest
import asyncio

async def test(bot_token, chat_id):
    @pytest.mark.asyncio
    async def test_is_port_open_success():
        print("Testing is_port_open with expected success...")
        assert await is_port_open("http://google.com", 80) == True
        print("Success case passed.")
    
    @pytest.mark.asyncio
    async def test_is_port_open_fail():
        print("Testing is_port_open with expected failure...")
        assert await is_port_open("http://example.com", 9999) == False
        print("Failure case passed.")
    
    
    @pytest.mark.asyncio
    async def test_is_service_running_success():
        print("Testing is_service_running with a running service...")
        assert await is_service_running("https://google.com") == True
        print("Running service case passed.")
    
    @pytest.mark.asyncio
    async def test_is_service_running_fail():
        print("Testing is_service_running with a non-running service...")
        assert await is_service_running("http://0.0.0.0.com") == False
    
    
    @pytest.mark.asyncio
    async def test_is_http_200_ok_success():
        print("Testing is_http_200_ok with a status 200 response...")
        assert await is_http_200_ok("http://google.com") == True
        print("Status 200 case passed.")
    
    @pytest.mark.asyncio
    async def test_is_http_200_ok_fail():
        print("Testing is_http_200_ok with a non-200 status response...")
        assert await is_http_200_ok("http://example.com/notfoundpage") == False
        print("Non-200 status case passed.")

    await send_telegram_message(bot_token, chat_id, f"Se puede hacer el PUSH ")
        
except asyncio.CancelledError:
    await send_telegram_message(bot_token, chat_id, f"La tarea ha sido cancelada.")
finally:
    await send_telegram_message(bot_token, chat_id, f"Se cancela el PUSH")



if __name__ == "__main__":
    
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    asyncio.run(test(bot_token, chat_id))


