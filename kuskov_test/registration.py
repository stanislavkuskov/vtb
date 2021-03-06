# -*- coding: utf-8 -*-

import telebot
from telebot import types
import re

API_TOKEN ='435200176:AAFWWdzzmP6FtRY5d32OJF4yeCjq-tRbBP4'

bot = telebot.TeleBot(API_TOKEN)
user_dict = {}
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add('Да', 'Нет')

class User:
    def __init__(self, phone):
        self.phone = phone
        #self.phone=None
        self.inn = None
        self.client = None

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Привет. Чтобы пользоваться ВТБ24 ботом
необходимо зарегистрироваться. Введите ваш номер телефона:
""")
    bot.register_next_step_handler(msg, process_phone_step)

# @bot.message_handler(regexp="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
def process_phone_step(message):
    try:
        chat_id = message.chat.id
        phone = message.text
        phone2 = message.text
        user = User(phone)
        user_dict[chat_id] = user
        if re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message.text):
            msg = bot.reply_to(message, 'Являетесь ли вы клиентом банка:',reply_markup=markup)
            bot.register_next_step_handler(msg, process_client_step)
        else:
            msg = bot.reply_to(message, 'Вы ввели неправильный номер телефона/ Введите еще раз:')
            bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')




def process_client_step(message):
    try:
        chat_id = message.chat.id
        client = message.text
        user = user_dict[chat_id]
        if (client == u'Да') or (client == u'Нет'):
            user.client = client
        else:
            raise Exception()

        msg = bot.reply_to(message, 'Введите ИНН:')
        bot.register_next_step_handler(msg, process_inn_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print e

def process_inn_step(message):
    try:
        chat_id = message.chat.id
        inn = message.text
        user = user_dict[chat_id]
        user.inn = inn
        bot.send_message(chat_id, u'Номер телефона: ' + str(user.phone) + '\n'u'Клиент банка: ' + user.client+ '\n'u'ИНН: ' + user.inn)
    except Exception as e:
        bot.reply_to(message, 'oooops')

bot.polling()
