from dotenv import load_dotenv
from aiogram import Bot
import os

load_dotenv()
bot = Bot(token=os.getenv("TOKEN")) #Бот здесь, так как я не придумал как ещё можно его импортировать в routers