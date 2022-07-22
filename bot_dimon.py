import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from bot_state import Check_category

tok = "1744432126:AAHDblqtDYp-J1LfTY3R6m-Lz1KfNV4KzgA"

storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token='1744432126:AAHDblqtDYp-J1LfTY3R6m-Lz1KfNV4KzgA', parse_mode='html')
dp = Dispatcher(bot, loop=loop, storage=storage)

category_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
teg_button = types.KeyboardButton(text='За катерогією')
self_category_button = types.KeyboardButton(text="За власним пошуковим запитом")
category_keyboard.add(teg_button).add(self_category_button)

work_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
homework_button = types.KeyboardButton(text="100% Віддалено")
hibryd_work_botton = types.KeyboardButton(text="Гібридно")
work_keyboard.add(homework_button, hibryd_work_botton)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer("Привіт, це Workado - твій помічник у пошуку віддаленої та гібридної роботи")
    await message.answer("Обери як будемо шукати тобі вакансії:", reply_markup=category_keyboard)
    await Check_category.one.set()


@dp.message_handler(state=Check_category.one)
async def type_of_work(message: types.Message):
    msg = message.text
    await message.answer("Оберіть тип роботи", reply_markup=work_keyboard)
    await Check_category.two.set()


@dp.message_handler(state=Check_category.two)
async def check_type(message: types.Message, state: FSMContext):
    msg = message.text
    if msg == "100% Віддалено":
        await state.finish()
    elif msg == "Гібридно":
        await message.answer("Оберіть місто для роботи")
        await state.finish()
    else:
        await message.answer("Вибач та я не знаю що це значить")
        await state.finish()


executor.start_polling(dp, skip_updates=True)
