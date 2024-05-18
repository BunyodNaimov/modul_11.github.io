import os
from aiogram import Dispatcher, F, Bot
from aiogram.methods import AnswerPreCheckoutQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, LabeledPrice, CallbackQuery, PreCheckoutQuery, ContentType
from keyboards import app_kb, buy_ikb
from dotenv import load_dotenv

load_dotenv()
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Salom", reply_markup=app_kb)


# @dp.callback_query(F.func(lambda call: call if call.data == "pay" else None))
@dp.message(Command('pay'))
async def order(msg: Message):
    print(msg.text)
    print(PROVIDER_TOKEN)
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali to'lov!",
        description="Telegram bot orqali to'lov qilishni o'rganyammiz!",
        need_name=True,
        need_phone_number=True,
        provider_token=PROVIDER_TOKEN,
        currency="UZS",
        payload="Ichki malumot",
        prices=[
            LabeledPrice(label="Tovar1", amount=10000),
            LabeledPrice(label="Tovar2", amount=10000)
        ],
        max_tip_amount=1000,
        suggested_tip_amounts=[100, 200, 300]
    )


@dp.pre_checkout_query()
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    print("pre_checkout_query", pre_checkout_q)
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message(F.func(lambda msg: msg.successful_payment if msg.successful_payment else 0))
async def successful_payment(message: Message):
    msg = f"""To'lov uchun raxmat!
    """
    await message.answer(msg)


@dp.message(F.func(lambda msg: msg.web_app_data.data if msg.web_app_data is not None else None))
async def get_btn(msg: Message):
    text = msg.web_app_data.data
    products = text.split("|")
    summa = 0
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
