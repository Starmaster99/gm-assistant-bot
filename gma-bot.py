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
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! 😃\n'
                                      'Я бот, который кидает за вас кубики. И больше не надо лезть в интернет! \n'
                                      'На выбор доступны: \n'
                                      '/d2    /d4    /d6    /d8    /d10    /d12    /d20    /d100')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! 😃\n'
                                      'Ты и другие любители D&D можете кидать все нужные для игры кубики с помощью '
                                      'одноимённых команд. Вот все доступные вам кубики:\n'
                                      '/d2    /d4    /d6    /d8    /d10    /d12    /d20    /d100')


@bot.callback_query_handler(func=lambda call: True)
def receive(call):
    if call.data == 'd2_repeat':
        d2(call.message)

    elif call.data == 'd4_repeat':
        d4(call.message)

    elif call.data == 'd6_repeat':
        d6(call.message)

    elif call.data == 'd8_repeat':
        d8(call.message)

    elif call.data == 'd10_repeat':
        d10(call.message)

    elif call.data == 'd12_repeat':
        d12(call.message)

    elif call.data == 'd20_repeat':
        d20(call.message)

    elif call.data == 'd100_repeat':
        d100(call.message)

    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(commands=['d2'])
def d2(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d2_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 2))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D2: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D2: Someone rolled {dicenum}')


@bot.message_handler(commands=['d4'])
def d4(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d4_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 4))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D4: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D4: Someone rolled {dicenum}')


@bot.message_handler(commands=['d6'])
def d6(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d6_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 6))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D6: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D6: Someone rolled {dicenum}')


@bot.message_handler(commands=['d8'])
def d8(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d8_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 8))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D8: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D8: Someone rolled {dicenum}')


@bot.message_handler(commands=['d10'])
def d10(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d10_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 10))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D10: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D10: Someone rolled {dicenum}')


@bot.message_handler(commands=['d12'])
def d12(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d12_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 12))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D12: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D12: Someone rolled {dicenum}')


@bot.message_handler(commands=['d20'])
def d20(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d20_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 20))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D20: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D20: Someone rolled {dicenum}')


@bot.message_handler(commands=['d100'])
def d100(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='🎲 Кинуть кубик ещё раз', callback_data='d100_repeat')
    markup.add(btn)
    dicenum = str(random.randint(1, 100))
    bot.send_message(message.chat.id, '<strong>О, восславтесь же, Великие Боги Рандома!</strong>\n'
                                      f'D100: <strong>{dicenum}</strong> оказалось на верхней грани кубика.',
                     parse_mode='html', reply_markup=markup)
    logging.info(f'D100: Someone rolled {dicenum}')


bot.polling(none_stop=True)
