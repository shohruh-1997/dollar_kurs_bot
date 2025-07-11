from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from dollar import kurs

API_TOKEN = "7318028110:AAHkWO7TtHgI8iOquU1VTgMiDPajr_30fMQ"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
# kurs


@dp.message(Command("start"))
async def menu_handler(message: types.Message):
    await message.answer("Salom bu dollar kursini aniqlab beruvchi bot\n"
                         "/kurs ni bosing")


@dp.message(Command("kurs"))
async def menu_handler(message: types.Message):
    await message.answer(f"Bugungi dollar kursi {kurs} so'm")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
