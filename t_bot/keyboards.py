from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

web_app = WebAppInfo(url='https://www.google.com')

app_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Mini App', web_app=web_app)]
], resize_keyboard=True)
