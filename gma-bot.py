import os
import random
import logging

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s : %(levelname)s ::: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

KEY = os.getenv('BOT_API_KEY')
bot = telebot.TeleBot(KEY)

logging.info('<---+--->\nStarting new session')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}! \n'
                                      'Я бот, который кидает за вас кубики. И больше не надо лезть в интернет! \n'
                                      'На выбор доступны: \n'
                                      '/d4,\n/d6,\n/d8,\n/d10,\n/d12,\n/d20,\n/d100\n', parse_mode='MARKDOWN')


@bot.callback_query_handler(func=lambda call: True)
def receive(call):
    if call.data == 'd4_repeat':
        d4(call.message)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(commands=['d4'])
def d4(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d4_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 4))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D4: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D4: {dicenum}')


bot.polling(none_stop=True)
