#vtbRObot

import telebot
TOKEN='435200176:AAFWWdzzmP6FtRY5d32OJF4yeCjq-tRbBP4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет. Введи номер телефона')

@bot.message_handler(regexp="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
def handle_message(message):

    # print (message.text)
    if message.text:
        print('номер корректен')


def main():
    bot.polling()



    pass
if __name__ == '__main__':
    main()