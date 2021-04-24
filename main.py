from telegram import ParseMode
from telegram.ext import Defaults
from telegram.ext import PicklePersistence
from telegram.ext import Updater

import handlers
from constants import TOKEN

updater = Updater(
    token=TOKEN,
    persistence=PicklePersistence(filename='data'),
    use_context=True,
    defaults=Defaults(
        parse_mode=ParseMode.HTML,
    ),
)
dp = updater.dispatcher
handlers.add_handlers(dp)
updater.start_polling(drop_pending_updates=True)
updater.idle()
