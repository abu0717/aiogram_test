from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware

router = Router()
router.message.outer_middleware(TestMiddleware())



class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Hello. \nYour id is {message.from_user.id}. \nYour name is {message.from_user.first_name}",
        reply_markup=kb.main,
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("This command is for /help")


@router.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer("OK")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMhZ0lR9lnHc3NJlnndEFgXvjxdmqMAAiveMRsBO0hK9ojf9Z2qmwYBAAMCAAN5AAM2BA",
        caption="Eto something",
    )


@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("You have chosen catalog")
    await callback.message.edit_text("Hello !", reply_markup=await kb.inline_cars())


@router.message(Command("reg"))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Enter your name")


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Enter your number")


@router.message(Reg.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(
        f"Thank you for registration. \nName: {data['name']}\nPhone Number: {data['number']}"
    )
    await state.clear()
