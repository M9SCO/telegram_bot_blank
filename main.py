import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler

from bin.data import const

from bot.cmds import start
#from bot.msg import
#from bot.btns import
#from bot.inln import

logging.basicConfig(filename='find_ exeption.log',
                    format='--- %(asctime)s ---\n%(filename)s %(levelname)s in line %(lineno)s \n%(message)s',
                    level=logging.ERROR)

def bot_start():
    updater = Updater(const["token"])  # , request_kwargs=REQUEST_KWARGS)
    dispatcher = updater.dispatcher

    '''cmds'''

    dispatcher.add_handler(CommandHandler('start', start))

    '''msg'''

    #dispatcher.add_handler(MessageHandler(Filters.all, message))

    """btns"""

    #updater.dispatcher.add_handler(CallbackQueryHandler(button))

    """inln"""

    #dispatcher.add_handler(InlineQueryHandler(inlinemode))

    """starting works"""
    print('KartotekaTheChwBot worked')
    updater.start_polling(clean=True)
    updater.idle()
if __name__ == '__main__':
    bot_start()