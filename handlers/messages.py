from aiogram import Dispatcher, types
from aiogram.types import Message
from config import API_URL, API_HEADERS, DEFAULT_MODEL
from state import get_current_model
import aiohttp
import logging

def register_messages_handlers(dp: Dispatcher):
    dp.message.register(filter_messages)

async def filter_messages(message: Message):
    current_model = get_current_model()

    data = {
        "model": current_model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": message.text
            }
        ],
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, headers=API_HEADERS, json=data) as response:
                response_json = await response.json()
                logging.info(f"API Response: {response_json}")

                if 'choices' not in response_json or len(response_json['choices']) == 0:
                    await message.answer('Произошла ошибка при получении ответа от модели. Пожалуйста, попробуйте снова.', parse_mode='Markdown')
                    return

                text = response_json['choices'][0]['message']['content']
                bot_text = text.split('</think>\n\n')

                if len(bot_text) > 1:
                    bot_text = bot_text[1]
                else:
                    bot_text = text  # Если разделитель не найден, используем весь текст

                await message.answer(bot_text, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Произошла ошибка при запросе к API: {e}")
        await message.answer('Произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте снова.', parse_mode='Markdown')