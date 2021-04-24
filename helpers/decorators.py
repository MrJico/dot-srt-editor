from typing import Callable

from telegram import Update
from telegram.ext import CallbackContext

from .context import file_opened
from constants import SUPERUSERS
from strings import get


def file(func: Callable) -> Callable:
    def decorator(update: Update, context: CallbackContext):
        if file_opened(context):
            return func(update, context)
        else:
            update.effective_message.reply_text(get('no_file_is_opened'))
    return decorator


def superusers(func: Callable) -> Callable:
    def decorator(update: Update,  context: CallbackContext):
        if update.effective_user.id in SUPERUSERS:
            return func(update, context)
    return decorator
