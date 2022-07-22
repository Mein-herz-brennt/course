from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='1744432126:AAHDblqtDYp-J1LfTY3R6m-Lz1KfNV4KzgA', parse_mode='html')
dp = Dispatcher(bot)

ls = [1, 2, 3, 4, 5]


def generate_keyboard(lst):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in lst:
        keyboard.add(types.KeyboardButton(text=f"{i}"))
    return keyboard


keyboard = types.ReplyKeyboardMarkup()
button = types.KeyboardButton(text="дай локацию", request_location=True)
keyboard.add(button)


@dp.message_handler(commands=['start', 'help'])
async def help_command(message: types.Message):
    await message.answer(f'Основна задача бота це вітати нових користувачів та пояснювати про освітні програми на '
                         f'Механіко-Математичному факультеті\n'
                         f'Основні команди бота:\n'
                         f'/math_info\n'
                         f'/stats_info\n'
                         f'/comp_mat_info\n'
                         f'/comp_meh_info\n'
                         f'/osvita_info\n'
                         f'--------------------------------------------------------\n'
                         f'Вся інформація отримана з офіційного сайту:\n'
                         f'Механіко-Математичного факультету', reply_markup=generate_keyboard(ls))
    msg = f"<i><b>Понеділок</b></i>\n" \
          f"1.<a href='https://meet.google.com/hzp-beaw-rxm'><b>Прога</b></a> Креневич\n" \
          f"2.<a href='https://meet.google.com/viv-bdti-gkk'><b>МатАн</b></a> Денисьєвський\n" \
          f"3.<a href='https://zoom.us/j/99775138366?pwd=T1pyZWw5YzMybUZSaEovOGJnTENCUT09'><b>Вдус</b></a> Горбань\n" \
          f"<i><b>Вівторок</b></i>\n"\
          f"2.<b>Англійська</b>\n"\
          f"3.<a href='https://zoom.us/j/2468975726?pwd=S3BqU0lnc0lGb3g4dzQvYmwvT0VDQT09'><b>ЛінАл</b></a> Ганюшкін\n"\
          f"4.<a href='https://us02web.zoom.us/j/6549501515?pwd=MG1vamM2OW5LSllMM2dDYWtYK1N1dz09'><b>МатАн</b></a> Радченко\n"\
          f"<i><b>Середа</b></i>\n" \
          f"1.<a href='https://meet.google.com/viv-bdti-gkk'><b>МатАн</b></a> Денисьєвський\n"\
          f"2.<a href='https://join.skype.com/fL27nSZ43OV6'><b>АнГеома</b></a> Журавльов\n" \
          f"3.<a href='https://us02web.zoom.us/j/84104335193?pwd=UFBMWFR0SXJodjhwV1l1VENxRUJtUT09'><b>ЛінАл</b></a> Безущак\n"\
          f"<i><b>Четвер</b></i>\n" \
          f"1.<a href='https://us04web.zoom.us/j/3162927964?pwd=UGFPdG9HUUo1QjdGSjFUVTBjU3Nldz09'><b>АнГеома</b></a> Прус\n"\
          f"2.<a href='https://meet.google.com/hzp-beaw-rxm'><b>Прога</b></a> Креневич\n" \
          f"3.<a href='https://us04web.zoom.us/j/2275305555?pwd=bkFsSGRLZjFVK0tJUkRscVFiL0V5UT09'><b>Дискретка</b></a> Яневич\n"\
          f"<i><b>П'ятниця</b></i>\n" \
          f"1.<a href='https://us02web.zoom.us/j/6549501515?pwd=MG1vamM2OW5LSllMM2dDYWtYK1N1dz09'><b>МатАн</b></a> Радченко\n"\
          f"3.<b>Англійська</b>\n" \
          f"4.<b>Англійська</b>\n"\
          f"------------------------------\n"\
          f"<i><b>Викладачі англійської</b></i>\n" \
          f"<a href='https://us04web.zoom.us/j/5563864234?pwd=UjBUZGdnUlQ2OE9ZMXRJSFRaOFJMZz09'><b>Летуновська</b></a>\n"\
          f"<a href='https://us04web.zoom.us/j/6729189895?pwd=WXhuTXZwM3BOYVc5bFg5eWEyMFBaQT09'><b>Мазур</b></a>\n"\
          f"<a href='https://us04web.zoom.us/j/71980205354?pwd=aVN0K3ZFd1BKOUlRcWVPLzhZRGRrQT09'><b>Ісаєва</b></a>\n"\
          f"<a href='https://us04web.zoom.us/j/7484218817?pwd=dXV3bEdiMSs1NGxTNkFoUnR5Tnpsdz09'><b>Андрійчук</b></a>\n"\
          f"<a href='https://join.skype.com/eU7r6FmbHG'><b>Ляшенко</b></a> Skype\n"\
          f"<a href='https://meet.google.com/wmc-bzsq-cu'><b>Малишева</b></a>\n"\
          f"<a href='https://us04web.zoom.us/j/2206835282?pwd=L1FLdEJLS09tTnRTYlBYZm9Ze'><b>Чугай</b></a>\n"

    await message.answer(msg)
@dp.message_handler(commands=['math_info'])
async def math_info_command(message: types.Message):
    await message.answer(f'Освітня програма <a href="http://www.mechmat.univ.kiev.ua/golovna/fakul-tet/matematy-ka'
                         f'/">Математика</a>\n'
                         f'Спеціалізації:\n'
                         f'   математичні методи обчислень\n'
                         f'   захисту інформації і машинне навчання\n'
                         f'   диференціальні рівняння, динамічні системи та математичні моделі\n'
                         f'   апроксимація і стохастика\n'
                         f'   ймовірність, інформація, обробка даних')


@dp.message_handler(commands=['stats_info'])
async def stats_info_command(message: types.Message):
    await message.answer(f"Освітня програма <a href='https://probability.knu.ua/'>Статистика</a>\n"
                         f"Спеціалізації:\n"
                         f"   актуарна та фiнансова математика\n"
                         f"   комп’ютерна статистика та аналіз даних\n"
                         f"   математична економiка")


@dp.message_handler(commands=['comp_mat_info'])
async def comp_math_info_command(message: types.Message):
    await message.answer(f"Освітня програма <a href='http://www.mechmat.univ.kiev.ua/golovna/fakul-tet/komp-yuterna"
                         f"-matematy-ka/'>Комп’ютерна математика</a>\n"
                         f"Спеціалізації:\n"
                         f"   аналіз даних\n"
                         f"   комп’ютерна математика")


@dp.message_handler(commands=['comp_meh_info'])
async def math_info_command(message: types.Message):
    await message.answer(f"Освітня програма <a href='http://www.mechmat.univ.kiev.ua/golovna/abiturientu/komp-yuterna"
                         f"-mexanika/'>Комп’ютерна механіка</a>\n"
                         f"Спеціалізації:\n"
                         f"   механіка\n"
                         f"   теоретична та прикладна механiка\n"
                         f"   механiка суцiльного середовища")


@dp.message_handler(commands=['osvita_info'])
async def math_info_command(message: types.Message):
    await message.answer(f"Освітня програма <a href='http://www.mechmat.univ.kiev.ua/golovna/fakul-tet/serednya"
                         f"-osvita/'>Середня освіта (Математика)</a>\n")


@dp.message_handler(content_types=["location"])
async def location(message: types.Message):
    print(message.location)
    print(message)


executor.start_polling(dp, skip_updates=True)
