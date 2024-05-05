import asyncio
import os
from aiogram import Bot
from dotenv import load_dotenv

# from aiogram.client.session.aiohttp import AiohttpSession


load_dotenv()
# session = AiohttpSession(proxy="http://proxy.server:3128")
# bot = Bot(token=BOT_TOKEN, session=session)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)


async def main():
    print("Starting .......")
    from handlers import dp
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
