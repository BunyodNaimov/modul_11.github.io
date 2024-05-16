from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from keyboards import app_kb, buy_ikb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=app_kb)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    text = msg.web_app_data.data
    products = text.split("|")
    summa = 0
    print(products)
    for i in range(len(products)):
        if len(products[i].split("/")) >= 3:
            title = products[i].split('/')[0]
            price = int(products[i].split('/')[1])
            quantity = int(products[i].split('/')[2])
            await msg.answer(text=f"Nomi: {title}\n"
                                  f"Narxi: {price}\n"
                                  f"Soni: {quantity}\n"
                                  f"Umumiy narxi: {quantity * price}$")
            summa += price * quantity
    await msg.answer(text=f"To'lanishi kerak: {summa}$", reply_markup=buy_ikb)
