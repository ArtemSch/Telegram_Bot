from aiogram import types
from loader import dp


@dp.message_handler(content_types="any")
async def bot_echo(message: types.Message):
    await message.answer('Прошу повторить набор, таких слов я ещё не знаю')




