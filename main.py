import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# Загружаем токен из переменной окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN переменная окружения не найдена!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Стартовое сообщение
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Привет! Это Telegram-бот Herchik Smart AI.\n\nНапиши /menu чтобы начать.")

# Пример команды меню
@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🧠 О боте", "📦 Тарифы", "📞 Поддержка")
    await message.answer("Выберите раздел:", reply_markup=keyboard)

# Обработка кнопок
@dp.message_handler(lambda message: message.text == "🧠 О боте")
async def about_bot(message: types.Message):
    await message.answer("💡 Этот бот помогает получить доступ к индикатору Smart Money Zones X на TradingView.")

@dp.message_handler(lambda message: message.text == "📦 Тарифы")
async def pricing(message: types.Message):
    await message.answer("💰 Доступные тарифы:\n\n"
                         "🔹 1 месяц — 99,000 сум\n"
                         "🔹 3 месяца — 199,000 сум\n"
                         "🔹 Lifetime — 499,000 сум\n\n"
                         "Оплата: Payme, Click, UzCard, USDT")

@dp.message_handler(lambda message: message.text == "📞 Поддержка")
async def support(message: types.Message):
    await message.answer("📩 Поддержка: @forex0042")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
