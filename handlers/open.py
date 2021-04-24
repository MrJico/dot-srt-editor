from os import path

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import send
from strings import get


def open(update: Update, context: CallbackContext):
    try:
        file_name = update.effective_message.text.split(maxsplit=1)[1]
    except IndexError:
        update.effective_message.reply_text(get('give_file_name'))
        return
    file_path = path.join(
        path.dirname(
            path.dirname(__file__),
        ), 'files', file_name,
    )
    if not path.isfile(file_path):
        update.effective_message.reply_text(get('file_does_not_exist'))
        return
    context.chat_data['file'] = file_path
    context.chat_data['line'] = 0
    update.effective_message.reply_text(get('opened'))
    send.current_line(update, context)


handlers = [[CommandHandler('open', open)]]
