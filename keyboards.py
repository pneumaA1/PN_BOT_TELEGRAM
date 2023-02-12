from telebot import types

# Start button
start_button = types.InlineKeyboardMarkup()
st_btn = types.InlineKeyboardButton(text='Start', callback_data='/start')

# Check button
check_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Проверить')
check_button.add(btn1)