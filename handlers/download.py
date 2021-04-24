from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from constants import ReplyMarkup
from helpers.decorators import file


@file
def download(update: Update, context: CallbackContext):
    update.effective_message.reply_document(
        document=open(context.chat_data['file'], 'rb'),
        reply_markup=ReplyMarkup.Remove,
    )


handlers = [[CommandHandler('download', download)]]
