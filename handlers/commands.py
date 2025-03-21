from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import MODELS
from state import get_current_model, set_current_model

def register_commands_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, CommandStart())
    dp.message.register(cmd_models, Command("models"))
    dp.message.register(choose_model, lambda message: message.text == "Выбрать модель")
    dp.message.register(list_models, lambda message: message.text == "Список моделей")
    dp.message.register(select_model, lambda message: message.text in MODELS.values())

async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Выбрать модель"), KeyboardButton(text="Список моделей")]
        ],
        resize_keyboard=True
    )
    await message.answer('Привет! Я бот с подключенной нейросетью, отправь свой запрос', reply_markup=keyboard, parse_mode='HTML')

async def cmd_models(message: types.Message):
    model_list = "\n".join([f"{key}: {value}" for key, value in MODELS.items()])
    await message.answer(f"Список доступных моделей:\n{model_list}", parse_mode='HTML')

async def select_model(message: Message):
    model = message.text
    set_current_model(model)
    await message.answer(f'Текущая модель: {model}', reply_markup=types.ReplyKeyboardRemove())

async def choose_model(message: Message):
    from keyboards import create_model_keyboard
    keyboard = create_model_keyboard(MODELS)
    await message.answer('Выберите модель:', reply_markup=keyboard)

async def list_models(message: Message):
    model_list = "\n".join([f"{key}: {value}" for key, value in MODELS.items()])
    await message.answer(f"Список доступных моделей:\n{model_list}", parse_mode='HTML')