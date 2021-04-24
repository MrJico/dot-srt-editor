from telegram.ext import CallbackContext


def file_opened(context: CallbackContext) -> bool:
    try:
        if context.chat_data['file']:
            return True
        return False
    except KeyError:
        return False


def next_line(context: CallbackContext):
    context.chat_data['line'] += 1


def prev_line(context: CallbackContext) -> bool:
    if context.chat_data['line'] != 0:
        context.chat_data['line'] -= 1
        return True
    return False
