from telegram.ext import CallbackContext

from constants import LOG_CHAT


def error(_, context: CallbackContext):
    context.bot.send_message(
        chat_id=LOG_CHAT,
        text=f'{type(context.error).__name__}: {context.error}',
    )


handlers = [[error, 'error']]
