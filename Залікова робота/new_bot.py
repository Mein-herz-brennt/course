import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from telebot import types
from malllib import Posht
import time

bot = telebot.TeleBot(config.TOKEN)

grafic = {'Парний': {'Понеділок': "1.Прога ООП Креневич "
                                  "А.П. https://meet.google.com/tch-ktzc-cfa \n "
                                  "2.3.Матан Петрова Т.О. Skype "
    ,
                     'Вівторок': '1.ЛА Кочубінська Є.А. https://meet.google.com/vgu-athq-hez \n'
                                 '2.Інгліш \n'
                                 'https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09\n'
                                 '3.ВДУС Набока С.В.  Ідентифікатор: 9507579405 Код: f0TD5m\n'
                                 'https://us04web.zoom.us/j/9507579405?pwd=MUtrUDRtMWN6NGl0eHdPZ1ZvM3ZvUT09',
                     'Середа': '1.ЛА  Кочубінська Є.А.https://meet.google.com/vgu-athq-hez\n'
                               '2.Дискретна практика  Лаврова О.Є. \n'
                               'https://us02web.zoom.us/j/89921173277?pwd=K2RDRlVkeEJab1BKTFQwU2JXNWF5Zz09\n'
                               'Ідентифікатор: 899 2117 3277 Код: eXi71u\n'
                               '3.ООП лаба Клевцовський А.В.\n'
                               'https://us04web.zoom.us/j/73346980432?pwd=cmRSNFNnUHlxbW5ZZkM2eDJOQzVTZz09',
                     'Четвер': '1.Дискретна  Олійник А.С. https://meet.google.com/kzs-dqyr-zwc\n'
                               '2.ЛА практика Білун С.В. \n'
                               'https://us04web.zoom.us/j/7604813302?pwd=MUJtd1ppdWJaaDZNNnpxbVRUd2U4dz09\n'
                               'Идентификатор: 760 481 3302 Код: 7p8cCd\n'
                               '3.Компмат Семенович К.О. Skype',
                     "П'ятниця": '1.3.Матан Петрова Т.О. Skype \n'
                                 '2.Інгліш \n'
                                 'https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09',
                     },
          'Непарний': {'Понеділок': "1.Прога ООП Креневич "
                                    "А.П. https://meet.google.com/tch-ktzc-cfa \n "
                                    "2.3.Матан : Петрова Т.О. Skype ",
                       'Вівторок': '1.2.Інгліш \n'
                                   'https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09\n'
                                   '3.ВДУС Набока С.В.  Ідентифікатор: 9507579405 Код: f0TD5m\n'
                                   'https://us04web.zoom.us/j/9507579405?pwd=MUtrUDRtMWN6NGl0eHdPZ1ZvM3ZvUT09',
                       'Середа': '1.ЛА Кочубінська Є.А.https://meet.google.com/vgu-athq-hez\n'
                                 '2.Дискретна практика  Лаврова О.Є. \n'
                                 'https://us02web.zoom.us/j/89921173277?pwd=K2RDRlVkeEJab1BKTFQwU2JXNWF5Zz09\n'
                                 'Ідентифікатор: 899 2117 3277 Код: eXi71u \n'
                                 '3.ООП лаба Клевцовський А.В.\n'
                                 'https://us04web.zoom.us/j/73346980432?pwd=cmRSNFNnUHlxbW5ZZkM2eDJOQzVTZz09',
                       'Четвер': '1.Дискретна  Олійник А.С. https://meet.google.com/kzs-dqyr-zwc\n'
                                 '2.ЛА практика Білун С.В. \n'
                                 'https://us04web.zoom.us/j/7604813302?pwd=MUJtd1ppdWJaaDZNNnpxbVRUd2U4dz09\n'
                                 'Идентификатор: 760 481 3302 Код: 7p8cCd\n'
                                 '3.Компмат Семенович К.О. Skype',
                       "П'ятниця": '1.3.Матан Петрова Т.О. Skype \n'
                                   '2.Інгліш\n'
                                   ' https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09',
                       }}

admin_inline_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
abutton1 = types.KeyboardButton(text='/change_subject')
abutton2 = types.KeyboardButton(text='/change_grafic')
admin_inline_keyboard.add(abutton1, abutton2)

role_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
role_button1 = types.KeyboardButton(text='/student')
role_button2 = types.KeyboardButton(text='/admin')
role_keyboard.add(role_button1, role_button2)

regime_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
regime_button1 = types.KeyboardButton(text='/clasic')
regime_button2 = types.KeyboardButton(text='/only_file')
regime_keyboard.add(regime_button1, regime_button2)


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 'Виберіть режим роботи:', reply_markup=regime_keyboard)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id,
                     "/clasic - стандартний peжим роботи ,# застосовний лише для особистих повідомлень \n"
                     "/only_file - режим роботи для групового чату, # надсилає файли з прив'язаної електронної пошти",
                     parse_mode='html')


@bot.message_handler(commands=['clasic'])
def command_clasic(message):
    bot.send_message(message.chat.id, "Вибери свою роль!", reply_markup=role_keyboard)


@bot.message_handler(commands=['admin'])
def command_admin(message):
    sms = bot.send_message(message.chat.id, "Вітаємо , о , найвеличніший! Будь ласка пройдіть автентифікацію!")
    sms2 = bot.send_message(message.chat.id, "Будь ласка введіть свій пароль:")
    bot.register_next_step_handler(sms, sms2, autentification)


# def autentification(message): password = '2002' if message.text == password: smm = bot.send_message(
# message.chat.id, "Вітаю ви успішно пройшли автентифікацію, і вкотре довели що це ви !", parse_mode='html') smm2 =
# bot.send_message(message.chat.id, "Виберіть які зміни ви хочете внести:", parse_mode='html',
# reply_markup=admin_inline_keyboard) bot.register_next_step_handler(smm, smm2, command_start) else: (
# message.chat.id, "Спробуйте ще раз !", parse_mode='html') bot.register_next_step_hand smm = bot.send_message(
# messler(smm, command_start)

@bot.message_handler(commands=['student'])
def command_user(message):
    mms = bot.send_message(message.chat.id, 'Не староста , але теж добре!')
    sms = bot.send_message(message.chat.id, "Вітаю, я ваш особистий розлад-бот ! ;)", parse_mode='html')
    sms2 = bot.send_message(message.chat.id, "Надішліть мені будь-яке повідомлення!", parse_mode='html')
    bot.register_next_step_handler(mms, sms, sms2, next_step)


@bot.message_handler(content_types=['text'])
def next_step(message):
    bot.reply_to(message, "Я надро простий щоб розуміти суть сказаного вами!")


@bot.message_handler(commands=['only_file'])
def command_only_file(message):
    bot.send_message(message.chat.id, 'OK')
    # bot.send_document(message.chat.id, )


if __name__ == "__main__":
    bot.polling(none_stop=True)
    while True:
        k = Posht('kriptongood81@gmail.com', 'good8181').login_and_download()
        time.sleep(2)
