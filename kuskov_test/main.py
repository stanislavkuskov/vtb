#vtbRObot
import telebot
from telebot import types

markup = types.ReplyKeyboardMarkup()
markup.row('Да', 'Нет')

TOKEN='435200176:AAFWWdzzmP6FtRY5d32OJF4yeCjq-tRbBP4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # регистрация пользователя в приложении?? в каком??
    # - Номер своего телефона (если бот сам не может определить номер);
    # - Является ли он клиентом Банка или нет. Если да - нужен вход в учетную
    # запись ВТБ24 Бизнес Онлайн. Если нет – может пользоваться
    # ограниченным функционалом для не-клиентов.

    # - Один из реквизитов, необходимых для определения ЮЛ/ИП, от имени
    # которого действует пользователь*.

    # ИНН свой? для регистрации

    bot.send_message(message.chat.id, 'Привет. Прошу выполнить простую процедуру регистрации')
    bot.send_message(message.chat.id, 'Введите номер телефона:')

@bot.message_handler(regexp="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
def handle_message(message):
    print (message)
    if message.text:
        print('номер корректен')
        bot.send_message(message.chat.id, "Являетесь ли вы клиентом ВТБ?", reply_markup=markup)

def main():
    bot.polling(none_stop=True)

    pass
if __name__ == '__main__':
    main()