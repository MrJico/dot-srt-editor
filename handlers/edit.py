import pysrt
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler

from constants import ReplyMarkup
from helpers import send
from helpers.decorators import file
from helpers.save import get_to_save
from strings import get


@file
def edit(update: Update, context: CallbackContext):
    file = pysrt.open(context.chat_data['file'], encoding='UTF-8')
    file[context.chat_data['line']].text = get_to_save(update.effective_message.text)
    file.save(context.chat_data['file'], encoding='UTF-8')
    update.effective_message.reply_text(
        text=get('edited'),
        reply_markup=ReplyMarkup.PrevNextEmptyDownload,
    )
    send.next_line(update, context)


handlers = [
    [MessageHandler(Filters.text & ~ Filters.command, edit)],
]
