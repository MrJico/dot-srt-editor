from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import send
from helpers.decorators import file


@file
def next(update: Update, context: CallbackContext):
    send.next_line(update, context)


handlers = [[CommandHandler('next', next)]]
