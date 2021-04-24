import importlib
import os

from telegram.ext import Dispatcher

modules, list_of_list_of_handlers = [], []

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith('.py'):
        if file not in ('__init__.py', '__main__.py'):
            modules.append(file[:-3])

for module in modules:
    list_of_list_of_handlers.append(
        importlib.import_module(f'handlers.{module}').handlers,
    )


def add_handlers(dp: Dispatcher):
    for list_of_handlers in list_of_list_of_handlers:
        for handler in list_of_handlers:
            if len(handler) == 1:
                dp.add_handler(handler[0])
            elif len(handler) == 2:
                if isinstance(handler[1], int):
                    dp.add_handler(handler[0], handler[1])
                elif isinstance(handler[1], str):
                    if handler[1] == 'error':
                        dp.add_error_handler(handler[0])
