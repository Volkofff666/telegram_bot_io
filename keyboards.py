from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_model_keyboard(models):
    keyboard = []
    row = []
    for key, value in models.items():
        row.append(KeyboardButton(text=value))
        if len(row) == 3:  # Разбиваем кнопки на ряды по 3
            keyboard.append(row)
            row = []
    if row:  # Добавляем последний неполный ряд, если есть
        keyboard.append(row)
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)