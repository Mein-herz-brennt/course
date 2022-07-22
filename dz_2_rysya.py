from aiogram import Bot, Dispatcher, executor, types

TOKEN = "1744432126:AAHDblqtDYp-J1LfTY3R6m-Lz1KfNV4KzgA"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

keyboard = types.InlineKeyboardMarkup()
button_da = types.InlineKeyboardButton(text="Так", callback_data="y")
button_net = types.InlineKeyboardButton(text="Ні", callback_data="n")
keyboard.add(button_da, button_net)


@dp.message_handler(commands=["start"])
async def marinka(message: types.Message):
    await message.answer("Ти не хочеш завтра піти погуляти?😇😅", reply_markup=keyboard)


@dp.callback_query_handler(text="y")
async def Yeas(call: types.CallbackQuery):
    await call.message.answer("ТОП🥰🥰🥰🥰")
    print("Yeas")


@dp.callback_query_handler(text="n")
async def noooo(call: types.CallbackQuery):
    await call.message.answer("😥😥😢😢😭😭😭😭😭")
    print("no")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
