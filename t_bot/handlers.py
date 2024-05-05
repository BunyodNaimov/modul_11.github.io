from aiogram import Dispatcher, types, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart

from keyboards import app_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=app_kb)


@dp.message(F.content_type.in_(ContentType.WEB_APP_DATA, ))
async def say(msg: types.Message):
    await msg.answer(msg.web_app_data.data)
