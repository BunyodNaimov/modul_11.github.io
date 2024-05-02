from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

from keyboards import app_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=app_kb)
