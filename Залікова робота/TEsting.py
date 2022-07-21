import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from telebot import types
from malllib import Posht
import time

bot = telebot.TeleBot(config.TOKEN, parse_mode='html')

admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
abutton1 = types.KeyboardButton(text='/change_subject')
abutton2 = types.KeyboardButton(text='/change_grafic')
admin_keyboard.add(abutton1, abutton2)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Виберіть режим роботи:')


@bot.message_handler(commands=['admin'])
def command_admin(message):
    sms = bot.send_message(message.chat.id, "Вітаємо , о , найвеличніший! Будь ласка пройдіть автентифікацію!")
    sms2 = bot.send_message(message.chat.id, "Будь ласка введіть свій пароль:")
    bot.register_next_step_handler(sms, sms2, autentification)


def autentification(message):
    password = '2002'
    if message.text == password:
        smm = bot.send_message(message.chat.id, "Вітаю ви успішно пройшли автентифікацію, і вкотре довели що це ви !")
        smm2 = bot.send_message(message.chat.id, "Виберіть які зміни ви хочете внести:", reply_markup=admin_keyboard)
        bot.register_next_step_handler(smm, smm2, command_start)
    else:
        smm = bot.send_message(message.chat.id, "Спробуйте ще раз !")
        bot.register_next_step_handler(smm, command_start)


if __name__ == "__main__":
    bot.polling()
