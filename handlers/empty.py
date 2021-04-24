import pysrt
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import send
from helpers.decorators import file


@file
def empty(update: Update, context: CallbackContext):
    file = pysrt.open(context.chat_data['file'], encoding='UTF-8')
    file[context.chat_data['line']].text = ''
    file.save(context.chat_data['file'], encoding='UTF-8')
    send.next_line(update, context)


handlers = [[CommandHandler('empty', empty)]]
