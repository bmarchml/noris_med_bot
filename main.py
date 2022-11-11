import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Database
TOKEN = '5631268168:AAH-bToDzRv9Dg8xPH0rkAZvlQYYvnpbnv4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exist(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Укажите Ваше ФИО')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы!', reply_markup=nav.mainMenu)

@dp.message_handler()
async def start(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ':
            pass

        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if (len(message.text) > 15):
                    await bot.send_message(message.from_user.id, 'ФИО слишком большое')
                elif '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, 'Вы ввели запрещенный символ')
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'Готово!')
                    await bot.send_message(message.from_user.id, 'Регистрация прошла успешно!', reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, 'Что?')

if __name__ == "__main__":
    executor.start_polling(db, skip_updates = True)