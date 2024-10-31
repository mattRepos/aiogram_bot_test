from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text = '♋'), KeyboardButton(text= '♐'), KeyboardButton(text = '♏'), KeyboardButton(text = '♎')],
    [KeyboardButton(text = '♈'), KeyboardButton(text = '♌'), KeyboardButton(text = '♓'), KeyboardButton(text = '♉')],
    [KeyboardButton(text = '♊'), KeyboardButton(text = '♍'), KeyboardButton(text = '⛎'), KeyboardButton(text = '♑')]
], resize_keyboard=True)

update = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text = 'Обновить', callback_data= 'Update')]
])