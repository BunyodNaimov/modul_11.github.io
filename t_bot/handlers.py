from aiogram import Dispatcher, types, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart, MagicData, callback_data
from aiogram.utils.magic_filter import MagicFilter

from keyboards import app_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=app_kb)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    text = msg.web_app_data.data
    products = text.split("|")
    print(products)
    for i in range(len(products)):
        print(products[i])
    title = products[0].split('/')[0]
    price = int(products[0].split('/')[1])
    quantity = int(products[0].split('/')[2])
    await msg.answer(text=f"Nomi: {title}\n"
                          f"Narxi: {price}"
                          f"Soni: {quantity}\n"
                          f"Umumiy narxi: {quantity * price}$")
