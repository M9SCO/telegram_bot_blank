import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler


from bin.data import const

from bot.cmds import start
from bot.msg import Messages
from bot.btns import Button
from bot.inln import Inline

logging.basicConfig(format='--- %(asctime)s ---\n%(filename)s %(levelname)s in line %(lineno)s \n%(message)s',
                    level=logging.ERROR)

def bot_start():
    updater = Updater(const.token)
    dispatcher = updater.dispatcher

    '''cmds'''

    dispatcher.add_handler(CommandHandler('start', start))

    '''msg'''

    dispatcher.add_handler(MessageHandler(Filters.all, Messages))

    """btns"""

    updater.dispatcher.add_handler(CallbackQueryHandler(Button))

    """inln"""

    dispatcher.add_handler(InlineQueryHandler(Inline))

    """starting works"""
    start_message= '''\
     　　／＞　    フ 
　　　　　| 　_　 _| 
　 　　　／`ミ _x 彡 
　　 　 /　　　 　 | 
　　　 /　 ヽ　　 ﾉ 
　／￣|　　 |　|　| 
　| (￣ヽ＿_ヽ_)_) 
　 ＼二つ

bot already worked
'''
    print(start_message)
    updater.start_polling(clean=True)
    # updater.idle()
if __name__ == '__main__':
    bot_start()