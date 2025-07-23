from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("🤖 এই বট দিয়ে তুমি মাল্টি গ্রুপ ম্যানেজ করতে পারো!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)