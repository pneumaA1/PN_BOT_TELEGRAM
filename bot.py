import telebot
import time
import get_info
from config import token
from keyboards import check_button
from HH_PARS import parse_data
from get_info import get_vacancies_info
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_bot(message):
	bot.send_message(message.chat.id, 'Hello',  reply_markup=check_button)

@bot.message_handler(regexp='Проверить')
def sent_vacancy(message):
	bot.send_message(message.from_user.id, "Поиск...")
	raw_data = parse_data()
	data = get_info.get_vacancies_info(raw_data)
	if not data:
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHoYJj4qwdN9critBpU8X9fJIT5tnJHgAClhkAAvXNUEth6IvJ8zDWMS4E')
		bot.send_message(message.chat.id, 'новых вакансий пока нет..')
	else:
		for text in data:
			time.sleep(0.8)
			bot.send_message(message.chat.id, text, parse_mode='html')


bot.infinity_polling()