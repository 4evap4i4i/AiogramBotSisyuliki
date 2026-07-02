from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

rout = Router()

@rout.message(CommandStart())
async def startcomm(message: Message):
    markup_start = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Домой', callback_data='page_home'),
            InlineKeyboardButton(text="Плейлист", callback_data='page_playlist')
        ]
    ])
    markup_playlist = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='малайфбилайк', callback_data='malaifbelike')
        ]
    ])

    builder = InlineKeyboardBuilder()
    builder.attach(InlineKeyboardBuilder.from_markup(markup_start))

    await message.answer_animation(animation="https://tenor.com/ru/view/кот-машет-рукой-котик-машет-ручкой-кот-машет-gif-11689341326546264835", caption='Дарова', reply_markup=builder.as_markup())

@rout.callback_query(event_name="page_home")
async def mvpstest():
    print("ура победа")