import pysrt
import pysrt.srttime
import pysrt.srtitem
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers import decorators
from helpers import send
from strings import get


@decorators.file
def new(update: Update, context: CallbackContext):
    args = update.effective_message.text.split()
    if len(args) != 3:
        update.effective_message.reply_text(get('usage_of_new_command'))
        return
    try:
        start = pysrt.srttime.SubRipTime.from_string(args[1])
        end = pysrt.srttime.SubRipTime.from_string(args[2])
    except pysrt.srttime.InvalidTimeString:
        update.effective_message.reply_text(get('invalid_time_provided'))
        return
    file = pysrt.open(context.chat_data['file'], encoding='UTF-8')
    file.append(pysrt.srtitem.SubRipItem(start=start, end=end))
    file.clean_indexes()
    file.save(context.chat_data['file'], encoding='UTF-8')
    context.chat_data['line'] = 0
    update.effective_message.reply_text(get('line_added'))
    send.current_line(update, context)


handlers = [[CommandHandler('new', new)]]
