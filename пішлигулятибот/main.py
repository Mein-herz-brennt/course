from aiogram import Bot, Dispatcher, executor, types

TOKEN = "1905664044:AAHng-M7s1yompWdVfpZYPV6qzVxhRFMV3o"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

keyb_yeas_or_no = types.InlineKeyboardMarkup()
button_yeas = types.InlineKeyboardButton(text="Ну пішли", callback_data="ok")
button_no = types.InlineKeyboardButton(text="Певно ні", callback_data="no")
keyb_yeas_or_no.add(button_yeas, button_no)


@dp.message_handler(commands="start")
async def go_guliatu_message(message: types.Message):
    await message.answer("Хм, може сходимо погуляти?", reply_markup=keyb_yeas_or_no)


@dp.callback_query_handler(text="ok")
async def message_yeas(call: types.CallbackQuery):
    pass