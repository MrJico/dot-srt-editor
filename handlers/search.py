import html

import pysrt
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from constants import ReplyMarkup
from helpers.decorators import file
from strings import get


@file
def search(update: Update, context: CallbackContext):
    try:
        query = update.effective_message.text.split(maxsplit=1)[1].lower()
    except IndexError:
        update.effective_message.reply_text(get('provide_search_query'))
        return
    file = pysrt.open(context.chat_data['file'], encoding='UTF-8')
    results = []
    for i in range(len(file)):
        no, line = i + 1, file[i]
        if len(results) > 10:
            break
        if query in line.text.lower():
            results.append([
                no, html.escape(
                    line.text.lower(),
                ).replace(query, f'<b>{query}</b>'),
            ])
    if len(results) == 0:
        update.effective_message.reply_text(
            text=get('no_results_found'),
            reply_markup=ReplyMarkup.Remove,
        )
        return
    update.effective_message.reply_text(
        text='\n'.join(
            (
                f'<b>{html.escape(result[1])}</b>\n└ {result[0]}'
                for result in results[:10]
            ),
        ),
        reply_markup=ReplyMarkup.Remove,
    )
    update.effective_message.reply_text(
        text=get('x_results_found').format(len(results)) if len(
            results,
        ) != 1 else get('one_result_found'),
    )
    if len(results) > 10:
        update.effective_message.reply_text(get('showing_first_ten_results'))


handlers = [[CommandHandler('search', search)]]
