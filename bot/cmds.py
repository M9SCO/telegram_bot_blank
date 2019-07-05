

def start(bot, update):
    mes = update.messages
    bot.send_message(chat_id=mes.chat_id, text='bot_worked')

print('commands opened')