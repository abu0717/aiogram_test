from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Catalog", callback_data="catalog")],
    [InlineKeyboardButton(text="Cart", callback_data="cart"),
    InlineKeyboardButton(text="Contact", callback_data="contacts")]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://youtu.be/qRyshRUA0xM?si=mZHPx4W8kvo82rcd")]
])

cars = ["tesla", "mercedes", "gm", "Volvo", "Audi"]
async def inline_cars():
    keyboar = InlineKeyboardBuilder()
    for car in cars:
        keyboar.add(InlineKeyboardButton(text=car, callback_data=f"car_{car}"))
    return keyboar.adjust(2).as_markup()