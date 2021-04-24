from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

import env


TOKEN = env.getenv('TOKEN')
SUPERUSERS = list(map(int, env.getenv('SUPERUSERS').split()))
LANGUAGE = env.getenv('LANGUAGE')
LOG_CHAT = int(env.getenv('LOG_CHAT'))


class ReplyMarkup:
    PrevNextEmptyDownload = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='/prev'),
                KeyboardButton(text='/next'),
            ],
            [
                KeyboardButton(text='/empty'),
            ],
            [
                KeyboardButton(text='/download'),
            ],
        ],
        resize_keyboard=True,
    )
    Download = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='/download'),
            ],
        ],
        resize_keyboard=True,
    )
    PrevNext = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='/prev'),
                KeyboardButton(text='/next'),
            ],
        ],
        resize_keyboard=True,
    )
    Remove = ReplyKeyboardRemove()
