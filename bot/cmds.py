

def start(bot, update):
    mes = update.message
    bot.send_message(chat_id=mes.chat_id, text='bot_worked')

print('commands detect')