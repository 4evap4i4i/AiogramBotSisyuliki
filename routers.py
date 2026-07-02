from pathlib import Path
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import bot
from random import choice

 # Обработчик событий
rout = Router()

# Стартовая страничка
markup_start = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Домой', callback_data='page_home'),
            InlineKeyboardButton(text="Плейлист", callback_data='page_playlist')
        ]
    ])

# Обработка /start
@rout.message(CommandStart())
async def rout_start(message: Message):
    global markup_start

    gifka = 'https://c.tenor.com/ojjiAPMVYwMAAAAd/tenor.gif'
    ayo = (
        "Дарова\n"
        "Скинь файл чтобы он появился в плейлисте\n"
        "Только mp3"
    )

    await message.answer_animation(animation=gifka, caption=ayo, reply_markup=markup_start)

# Обработка кнопки "Домой"
@rout.callback_query(F.data == "page_home")
async def rout_home(callback: CallbackQuery):
    global markup_start

    await callback.message.edit_reply_markup(reply_markup=markup_start)

# Обработка кнопки "Плейлист"
@rout.callback_query(F.data == "page_playlist")
async def rout_playlist(callback: CallbackQuery):
    audio_dir = Path("./audio")

    markup_playlist = InlineKeyboardBuilder()

    markup_playlist.button(text="Домой", callback_data="page_home")
    markup_playlist.button(text='Случайность', callback_data='audio_random')
    for i in audio_dir.iterdir():
        markup_playlist.button(text=i.name, callback_data=f"audio_fixed{i.name}")

    markup_playlist.adjust(2,3)

    await callback.message.edit_reply_markup(reply_markup=markup_playlist.as_markup())

# Обработка кнопки "Случайность"
@rout.callback_query(F.data == "audio_random")
async def rout_sendrand(callback: CallbackQuery):
    audio_dir = Path("./audio")

    audios = [i for i in audio_dir.iterdir()]
    audio_random = str(choice(audios))[5:]
    audio_random = FSInputFile(f"./audio/{audio_random}")
    await callback.message.answer_audio(audio=audio_random)

# Обработка кнопки со звуком
@rout.callback_query(F.data.startswith("audio_fixed"))
async def rout_sendfixd(callback: CallbackQuery):
    audio = str(callback.data)[11:]
    audio = FSInputFile(f"./audio/{audio}")

    await callback.message.answer_audio(audio=audio)

# Обработка аудио файла (скачка в папку audio)
@rout.message(F.audio)
async def rout_save(message: Message):
    audio = message.audio

    audio_name = str(audio.file_name)[:5]
    if not audio_name.endswith(".mp3"):
        audio_name += ".mp3"

    await bot.download(audio ,destination=f"./audio/{audio_name}")