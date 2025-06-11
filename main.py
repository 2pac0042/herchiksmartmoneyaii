import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.dispatcher.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.answer("Привет! Это Herchik Smart Money AI бот. 🤖")

@dp.message_handler()
async def echo(message: Message):
    await message.answer("Я получил твоё сообщение: " + message.text)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
