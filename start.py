from aiogram import Bot, Dispatcher
import asyncio
from routers import rout
from config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(rout)
    print("готовченко")
    await dp.start_polling(bot)

asyncio.run(main())