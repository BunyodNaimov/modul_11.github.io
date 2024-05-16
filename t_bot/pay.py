from aiogram import Bot

from aiogram.types import Message, LabeledPrice


async def order(msg: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali sotib olish!",
        description="Telegram bot orqali to'lov qilishni o'rganyammiz!",
        payload="Ichki malumot",  # Foydalanuvchiga ko'rinmiydi
        provider_token="ukassa dan olingan token",
        currency="sum",
        prices=[
            LabeledPrice(label="NDS", amount=1),
            LabeledPrice(label="Skidka", amount=-2),
            LabeledPrice(label="Bonus", amount=-3),
        ],
        max_tip_amount=100,  # summa chayevix
        suggested_tip_amounts=[10, 15, 20, 25], # predlagaymiy summa chayevix
        start_parameter="nztcoder", #
        provider_data=None,
        photo_url='https/',
        photo_size=100,
        photo_width=100,
        photo_height=100,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=False,

    )
