import pysrt
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import decorators
from helpers import send
from strings import get


@decorators.file
def line(update: Update, context: CallbackContext):
    try:
        line = update.effective_message.text.split(maxsplit=1)[1]
    except IndexError:
        update.effective_message.reply_text(get('give_line_number'))
        return
    try:
        line = int(line) - 1
    except ValueError:
        update.effective_message.reply_text(get('give_line_number'))
        return
    file = pysrt.open(context.chat_data['file'], encoding='UTF-8')
    if line not in range(len(file)):
        update.effective_message.reply_text(
            get('line_x_does_not_exist').format(line + 1),
        )
        return
    context.chat_data['line'] = line
    update.effective_message.reply_text(
        get('moved_to_line_x').format(line + 1),
    )
    send.current_line(update, context)


handlers = [[CommandHandler('line', line)]]
