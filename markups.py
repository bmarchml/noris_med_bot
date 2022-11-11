from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton(' Профиль')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile)