import html

import pysrt
from telegram import Update
from telegram.ext import CallbackContext

from .context import next_line as _next_line
from constants import ReplyMarkup
from strings import get


def current_line(update: Update, context: CallbackContext):
    try:
        sub = pysrt.open(
            context.chat_data['file'], encoding='UTF-8',
        )[context.chat_data['line']]
    except KeyError:
        context.chat_data.clear()
        update.effective_message.reply_text(
            text=get('end_of_file'),
            reply_markup=ReplyMarkup.Download,
        )
        return
    if not sub.text.strip().rstrip():
        update.effective_message.reply_text(get('empty_line'))
    else:
        update.effective_message.reply_text(html.escape(sub.text))
    h = (
        '0' if len(str(sub.start.hours)) == 1 else ''
    ) + str(sub.start.hours)
    m = (
        '0' if len(str(sub.start.minutes)) ==
        1 else ''
    ) + str(sub.start.minutes)
    s = (
        '0' if len(str(sub.start.seconds)) ==
        1 else ''
    ) + str(sub.start.seconds)
    start_time = f'{h}:{m}:{s}'
    update.effective_message.reply_text(
        text=get('line_info').format(
            context.chat_data['line'] + 1,
            start_time,
        ),
        reply_markup=ReplyMarkup.PrevNextEmptyDownload,
    )


def next_line(update: Update, context: CallbackContext):
    _next_line(context)
    current_line(update, context)
