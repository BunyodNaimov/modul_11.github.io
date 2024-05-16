import asyncio
from dotenv import load_dotenv

# from aiogram.client.session.aiohttp import AiohttpSession


load_dotenv()
# session = AiohttpSession(proxy="http://proxy.server:3128")
# bot = Bot(token=BOT_TOKEN, session=session)



async def main():
    print("Starting .......")
    from handlers import dp
    from handlers import bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
