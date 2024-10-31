from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from datetime import datetime

from app.keybord import main as kb, update as up

import horoscope as hor
import random

class Reg(StatesGroup):
    name = State()
    zodiac_sign = State()

router = Router()

def format_text():
    horoscope_text = random.choice(list(hor.horoscope.values()))
    time = datetime.now().strftime('%M-%D')
    f_text = f'{time}\n{horoscope_text}'
    return f_text

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Здравствуйте! Перед началом использования бота необходимо зарегистрироваться')
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')

@router.message(Command ('update'))
async def cmd_update(message: Message):
    f_text = format_text()
    await message.answer(f_text, reply_markup= up)
###
@router.message(Command('change_zodiac'))
async def change_zodiac(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state in [Reg.name.state, Reg.zodiac_sign.state]:
        await state.set_state(Reg.zodiac_sign)
        await message.answer('Выберите знак зодиака из представленных ниже', reply_markup=kb)
    else:
        await message.answer('Сначала зарегистрируйтесь, введя команду /start')
###
@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.zodiac_sign)
    await message.answer('Выберите знак зодиака из представленных ниже', reply_markup=kb)

zodiac_mapping = {
    '♈', '♉', '♊', '♋', '♌', '♍',
    '♎', '♏', '♐', '♑', '♒', '♓'
}

def is_zodiac_sign(message: types.Message):
    return message.text in zodiac_mapping

@router.message(Reg.zodiac_sign, is_zodiac_sign)
async def reg_zodiac(message: Message, state: FSMContext):
    await state.update_data(zodiac_sign=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, ваше имя - {data["name"]} и знак зодиака {data["zodiac_sign"]}! Регистрация завершена')


    horoscope_text = random.choice(list(hor.horoscope.values()))

    await message.answer(horoscope_text, reply_markup=up)


@router.message(is_zodiac_sign)
async def text(message: types.Message):
    f_text = format_text()
    await message.answer(f_text, reply_markup=up)

@router.callback_query(F.data == 'Update')
async def update(callback: CallbackQuery):
    f_text = format_text()
    await callback.message.answer(f_text, reply_markup= up)

@router.message(F.text)
async def somethink(message: Message):
    await message.answer("Извините, я не понял")
