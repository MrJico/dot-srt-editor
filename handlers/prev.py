from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import send
from helpers.context import prev_line
from helpers.decorators import file


@file
def prev(update: Update, context: CallbackContext):
    if prev_line(context):
        send.current_line(update, context)


handlers = [[CommandHandler('prev', prev)]]
