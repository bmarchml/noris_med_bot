import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Databasse

TOKEN = '5548537514:AAGlKbQi0DgjlHCDaZq83yG0xwcXwE-TqCo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Databasse('db.db')


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Укажите Ваше ФИО')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы!', reply_markup=nav.mainMenu)


@dp.message_handler(content_types=["text"])
async def name(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Профиль':
            pass
        else:
            if db.get_signup(message.from_user.id) == "set_nickname":
                if len(message.text) > 33:
                    await bot.send_message(message.from_user.id, 'ФИО слишком большое')
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, 'Вы ввели запрещенный символ')
                elif len(message.text) < 33:
                    db.set_user_name(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'Введено')
                    await bot.send_message(message.from_user.id, 'Ваше ФИО внесенно в профиль')

                else:
                    await bot.send_message(message.from_user.id, 'Что?')


@dp.message_handler(content_types=["text"])
async def male(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ваш пол')
    if db.get_signup1(message.from_user.id) == "set_male":
        if len(message.text) > 9:
            await bot.send_message(message.from_user.id, 'слишком длинное')
        elif '@' in message.text or '/' in message.text:
            await bot.send_message(message.from_user.id, 'Вы ввели запрещенный символ')
        else:
            db.set_user_male(message.from_user.id, message.text)
            db.set_signup1(message.from_user.id, 'Введено')
            await bot.send_message(message.from_user.id, 'Ваш пол внесен в профиль!', reply_markup=nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, 'Что?')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
