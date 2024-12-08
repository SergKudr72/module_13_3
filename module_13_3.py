from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = "token_bot???"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

#Проверка по text:
@dp.message_handler(text = ['UrbanStudent'])
async def urban_student(message):
    print("Hi, URBANSTUDENT!")
    await message.answer(f'Hi, {message.text.upper()}!')

@dp.message_handler()
async def all_messange(messange):
    print("Введите команду /start, чтобы начать общение.")
    await messange.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
