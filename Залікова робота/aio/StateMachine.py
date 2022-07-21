from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin_state(StatesGroup):
    password = State()
    nice_try = State()


class Rozlad_state(StatesGroup):
    week = State()
    day = State()


class Only_State(StatesGroup):
    first = State()
    second = State()
    third = State()
