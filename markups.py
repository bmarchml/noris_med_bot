from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton(' Профиль ')
btnSmena = KeyboardButton('Сменить ')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSmena)
