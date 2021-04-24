from os import path

from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Filters
from telegram.ext import MessageHandler

from helpers.decorators import superusers
from strings import get


@superusers
def upload(update: Update, _):
    file_name = update.effective_message.document.file_name.lower().replace(' ', '_')
    file_path = path.join(
        path.dirname(
            path.dirname(__file__),
        ), 'files', file_name,
    )
    if path.isfile(file_path):
        update.effective_message.reply_text(get('file_exists'))
        return
    elif not file_path.endswith('.srt'):
        return
    else:
        update.effective_message.document.get_file().download(file_path)
        update.effective_message.reply_text(
            text=get('uploaded'),
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(
                            text=f'/open {file_name}',
                        ),
                    ],
                ],
            ),
        )
        update.effective_message.reply_text(get('use_button_to_open'))


handlers = [[MessageHandler(Filters.document, upload)]]
