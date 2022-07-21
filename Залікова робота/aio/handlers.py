import os.path
from malllib import Posht
from main import bot, dp
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram import types
from StateMachine import Admin_state, Only_State
from aiogram.dispatcher import FSMContext
# import time

rozlad = {'1': '8.40-10.15', '2': '10.35-12.10', '3': '12.20-13.55'}

grafic = {'Парний': {'Понеділок': "1.Прога ООП Креневич \n"
                                  "А.П. https://meet.google.com/tch-ktzc-cfa \n "
                                  "2.3.Матан Петрова Т.О. Skype ",
                     'Вівторок': '1.ЛА Кочубінська Є.А. https://meet.google.com/vgu-athq-hez \n'
                                 '2.Інгліш \n'
                                 'https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09\n'
                                 '3.ВДУС Набока С.В.  Ідентифікатор: 9507579405 Код: f0TD5m\n'
                                 'https://us04web.zoom.us/j/9507579405?pwd=MUtrUDRtMWN6NGl0eHdPZ1ZvM3ZvUT09',
                     'Середа': '1.ЛА  Кочубінська Є.А.https://meet.google.com/vgu-athq-hez\n'
                               '2.Дискретна практика  Асроров Ф.А. \n'
                               'https://us05web.zoom.us/j/9533137046?pwd=VTYvQXBpVmZMKytGNnNjdlFPK00vZz09\n'
                               'Ідентифікатор: 953 313 7046 Код: H0r1jg\n'
                               '3.ООП лаба Клевцовський А.В.\n'
                               'https://us04web.zoom.us/j/73346980432?pwd=cmRSNFNnUHlxbW5ZZkM2eDJOQzVTZz09',
                     'Четвер': '1.Дискретна  Олійник А.С. https://meet.google.com/kzs-dqyr-zwc\n'
                               '2.ЛА практика Білун С.В. \n'
                               'https://us04web.zoom.us/j/7604813302?pwd=MUJtd1ppdWJaaDZNNnpxbVRUd2U4dz09\n'
                               'Идентификатор: 760 481 3302 Код: 7p8cCd',
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
                                 '2.Дискретна практика  Асроров Ф.А. \n'
                                 'https://us05web.zoom.us/j/9533137046?pwd=VTYvQXBpVmZMKytGNnNjdlFPK00vZz09\n'
                                 'Ідентифікатор: 953 313 7046 Код: H0r1jg \n'
                                 '3.ООП лаба Клевцовський А.В.\n'
                                 'https://us04web.zoom.us/j/73346980432?pwd=cmRSNFNnUHlxbW5ZZkM2eDJOQzVTZz09',
                       'Четвер': '1.Дискретна  Олійник А.С. https://meet.google.com/kzs-dqyr-zwc\n'
                                 '2.ЛА практика Білун С.В. \n'
                                 'https://us04web.zoom.us/j/7604813302?pwd=MUJtd1ppdWJaaDZNNnpxbVRUd2U4dz09\n'
                                 'Идентификатор: 760 481 3302 Код: 7p8cCd\n'
                                 '3.Компмат Семенович К.О. Skype',
                       "П'ятниця": '1.3.Матан Петрова Т.О. Skype \n'
                                   '2.Інгліш\n'
                                   'https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09',
                       }}

week_keyboard = types.ReplyKeyboardMarkup()
week_button = types.KeyboardButton(text="Вибрати тиждень")

# парність тижня клава
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_par = types.KeyboardButton(text='Парний')
button_nopar = types.KeyboardButton(text='Непарний')
keyboard1.add(button_par, button_nopar)
# день тижня клава
keyboard2 = types.ReplyKeyboardMarkup()
button_monday = types.KeyboardButton(text='Понеділок')
button_tuesday = types.KeyboardButton(text='Вівторок')
button_wednesday = types.KeyboardButton(text='Середа')
button_thursday = types.KeyboardButton(text='Четвер')
button_friday = types.KeyboardButton(text="П'ятниця")
keyboard2.add(button_monday, button_tuesday, button_wednesday, button_thursday, button_friday)
# час пар
inline_keyboard = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text='1', callback_data='1')
button2 = types.InlineKeyboardButton(text='2', callback_data='2')
button3 = types.InlineKeyboardButton(text='3', callback_data='3')
inline_keyboard.add(button1, button2, button3)

regime_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
regime_button1 = types.KeyboardButton(text='/clasic')
regime_button2 = types.KeyboardButton(text='/only_file')
regime_keyboard.add(regime_button1, regime_button2)

role_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
role_button1 = types.KeyboardButton(text='/student')
role_button2 = types.KeyboardButton(text='/admin')
role_keyboard.add(role_button1, role_button2)

admin_inline_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
abutton1 = types.KeyboardButton(text='/change_subject')
abutton2 = types.KeyboardButton(text='/change_grafic')
admin_inline_keyboard.add(abutton1, abutton2)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: Message):
    await message.answer('Виберіть режим роботи:', reply_markup=regime_keyboard)
    await message.answer("/clasic - стандартний peжим роботи ,\n# застосовний лише для особистих повідомлень \n"
                         "/only_file - режим роботи для групового чату,\n # надсилає файли з прив'язаної електронної\n"
                         "пошти")


@dp.message_handler(commands=['clasic'])
async def command_classic(message):
    await message.answer("Вибери свою роль!", reply_markup=role_keyboard)


@dp.message_handler(commands=['admin'], state=None)
async def command_admin(message: Message):
    await message.answer("Вітаємо , о , найвеличніший! Будь ласка пройдіть автентифікацію!")
    await message.answer("Будь ласка введіть свій пароль:")
    # await bot.register_next_step_handler(sms, sms2, autentification)
    await Admin_state.password.set()


@dp.message_handler(state=Admin_state.password)
async def autentification(message: Message, state: FSMContext):
    inputing_password = message.text
    password = '1234'
    if inputing_password == password:
        await message.answer("Вітаю ви успішно пройшли автентифікацію, і вкотре довели що це ви !")
        await message.answer("Виберіть які зміни ви хочете внести:", reply_markup=admin_inline_keyboard)
        # await bot.register_next_step_handler(smm, smm2, command_start)
        await Admin_state.nice_try.set()
    else:
        await message.answer("Тупак, ти ж студент /student")
        # await bot.register_next_step_handler(smm, command_start)
        await state.finish()


@dp.message_handler(commands=['student'])
async def command_user(message: Message):
    await message.answer("Вітаю, я ваш особистий розлад-бот ! ;)")
    await message.answer('Який зараз тиждень?', reply_markup=keyboard1)
    # await bot.register_next_step_handler(mms, sms, sms2, next_step)


@dp.message_handler(text=['Парний', 'Непарний'])
async def why_week(message):
    global par
    weekend = message.text
    if weekend == 'Парний':
        par = True
        await message.answer('Який сьогодні день?', reply_markup=keyboard2)
        # bot.register_next_step_handler(sms, lambda sms: why_day(par, sms))
    elif weekend == 'Непарний':
        par = False

        await message.answer('Який сьогодні день?', reply_markup=keyboard2)
    # bot.register_next_step_handler(sms, lambda sms: why_day(par, sms))


@dp.message_handler(text=["Понеділок", "Вівторок", "Середа", "Четвер"])
async def why_day(message: Message):
    global par
    day = message.text
    if par:
        rozklad = grafic['Парний'][day]
    else:
        rozklad = grafic['Непарний'][day]
    await message.answer(rozklad, reply_markup=inline_keyboard)


@dp.message_handler(text="П'ятниця")
async def friday(message: Message):
    global par
    day = message.text
    if par:
        rozklad = grafic['Парний'][day]
    else:
        rozklad = grafic['Непарний'][day]
    await message.answer(rozklad, reply_markup=inline_keyboard)
    if par:
        par = False
        await message.answer('Настав не парний тиждень')
    else:
        par = True
        await message.answer('Настав парний тиждень')


@dp.callback_query_handler(lambda call: True)
async def non_time(call: CallbackQuery):
    answer = ''
    if call.data == '1':
        answer = rozlad['1']
    elif call.data == '2':
        answer = rozlad['2']
    elif call.data == '3':
        answer = rozlad['3']
    await bot.answer_callback_query(call.id, answer)


# @dp.message_handler(content_types=['text'])
# async def next_step(message: Message):
# await message.answer("Я надро простий щоб розуміти суть сказаного вами!")


@dp.message_handler(commands=['only_file'])
async def command_only_file(message: Message):
    await message.reply('OK')
    await message.answer('Введіть адресу електронної пошти')
    await Only_State.first.set()


@dp.message_handler(state=Only_State.first)
async def get_mail(message: Message):
    global mail
    mail = message.text
    await message.answer('Введіть пароль до електронної пошти')
    await Only_State.second.set()


@dp.message_handler(state=Only_State.second)
async def get_mail_password(message: Message):
    global mail_password, filePath
    mail_password = message.text
    await message.answer('Тепер ми у режимі лише для файлів, використання інших режимів у груповому чаті заборонено')

    file = Posht(mail, mail_password).login_and_download()
    filename = InputFile(fr'C:\Users\icaev\Desktop\РАЗНОЕ\програмування\Залікова робота\aio\{file}', file)
    if os.path.isfile(file):
        await message.answer_document(filename)
