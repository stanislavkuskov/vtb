#vtbRObot

import telebot
TOKEN='435200176:AAFWWdzzmP6FtRY5d32OJF4yeCjq-tRbBP4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

def main():
    bot.polling()



    pass
if __name__ == '__main__':
    main()