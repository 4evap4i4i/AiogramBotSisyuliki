from aiogram import Dispatcher
import asyncio
from routers import rout
from config import bot

async def main():
    dp = Dispatcher()
    dp.include_router(rout) # Обязательно добавить роуты в диспатчер, так как иначе они не будут обрабатываться
    await dp.start_polling(bot)

asyncio.run(main())