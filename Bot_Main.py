import logging
from telegram.ext import CommandHandler, MessageHandler, Filters

from bin import updater
from Bot_Commands import start
from Bot_Messages import callback_text_messages


logging.basicConfig(format='--- %(asctime)s ---\n%(filename)s %(levelname)s in line %(lineno)s \n%(message)s',
                    level=logging.ERROR)

dispatcher = updater.dispatcher

'''Hadlers'''

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, callback_text_messages))
dispatcher.add_handler(MessageHandler(Filters.all, start))
updater.start_polling()
updater.idle()
