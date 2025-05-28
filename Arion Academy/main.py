from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = '8009596428:AAEGYJild4leGK688ceb482CHR1fb82Lr7U'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(
            text="🚀 Открыть Академию",
            web_app=WebAppInfo(url="https://arionacademy.vercel.app")  # сюда позже вставим ссылку
        )
    )
    await message.answer("Добро пожаловать в ARION ACADEMY!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
