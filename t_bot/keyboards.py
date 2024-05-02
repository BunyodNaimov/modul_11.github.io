from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

web_app = WebAppInfo(url='https://bunyodnaimov.github.io/modul_11.github.io/')

app_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Mini App', web_app=web_app)]
], resize_keyboard=True)
