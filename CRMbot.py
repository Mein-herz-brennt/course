from aiogram import Bot, Dispatcher, executor, types
import json
from datetime import datetime
import time

bot = Bot(token='1744432126:AAHDblqtDYp-J1LfTY3R6m-Lz1KfNV4KzgA', parse_mode='html')
dp = Dispatcher(bot)

info_about_users = {}
info = {"data": []}


def generate_keyboard(lst):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in lst:
        keyboard.add(types.KeyboardButton(text=f"{i}"))
    return keyboard


# def generate_inline_keyboard(dct):
#     inline_keyboard = types.InlineKeyboardMarkup()
#     with open("nice.text", "r") as f:
#         print(f.readlines())
#         # for key in dct.keys():
#             button = types.InlineKeyboardButton(text=f"{dct[key]}", callback_data=)

while True:
    @dp.message_handler(commands=["start"])
    async def command_start(message: types.Message):
        global info_about_users
        id_ = message.from_user.id
        # all_info = {
        #     "id_": f"{message.from_user.id}",
        #     "price": f"{3000}",
        #     "tag": f"@{message.from_user.username}"
        # }
        # info_about_users[f"@{message.from_user.username}"] = all_info
        # print(info_about_users)
        if id_ == 789402487 or 215037238:
            await message.answer("здравствуй хазяин")
        else:
            await message.answer("Привет незнакомец")
        await message.answer("1")


    @dp.message_handler(commands=["help"])
    async def command_start(message: types.Message):
        await message.answer("Я бот создан для того чтоб помочь вам и напоминать о оплате сьёмного жилья")


    @dp.message_handler(commands=["new_user"])
    async def adress_command(message: types.Message):
        await message.answer("надішліть адресу")


    @dp.message_handler(content_types=["text"])
    async def all_text(message: types.Message):
        if message.text.startswith("Вул."):
            global vyl
            vyl = message.text
            await message.answer("Надішліть контакт майбутнього орендаря")
        else:
            global name
            name = message.text
            print("1")


    @dp.message_handler(content_types=["contact"])
    async def contact_command(message: types.Message):
        global vyl, info
        # contact = message.contact
        a = {
            'first_name': f"{message.contact.first_name}",
            'phone_number': f"{message.contact.phone_number}",
            'user_id': f"{message.contact.user_id}",
            'adres': f"{vyl}"
        }
        with open("nice.json", "w") as f:
            info["data"].append(a)
            json.dump(info, f, indent=3)
        # print(info["data"].append(a))
        # with open("nice.json", "w") as file:  # )file.write(f"{info_about_users}\n"
        #     json.dump(info, file)
        # file.write(",\n")
        # with open("nice.text", "a") as file: file.write(f"{contact}\n")
        print(message.contact)


    @dp.message_handler(content_types=["photo"])
    async def command_photo(message: types.Message):
        global info_about_users, name
        if message.from_user.id != 789402487:
            await message.forward(chat_id=789402487)
        else:
            i_d = "id_"
            await message.forward(chat_id=f"{info_about_users[name][i_d]}")

    while True:
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")  # "%d/%m/%Y
        timee = ['11:30:00', '14:00:00', '17:30:00']
        time2 = ['20:07:00']
        print(dt_string)
        if time2 == dt_string.split(' ')[0]:
            print('Сообщение отправлено', dt_string.split(' ')[1])
            print('Просьба пересчитать кассу сравнить с X-отчетом,и дать ответ в ЛС @nastya_dp')
            time.sleep(0.5)
        else:
            continue

    executor.start_polling(dp, skip_updates=True)
