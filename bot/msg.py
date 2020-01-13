def Messages(bot, update):
    mes = update.message
    if mes.text:
        text(bot, update)
    if mes.sticker:
        sticker(bot, update)
    if mes.new_chat_members:
        new_chat_member(bot, update)
    if mes.left_chat_member:
        left_chat_member(bot, update)


""" --- -- --- """


def text(bot, update):
    pass


def sticker(bot, update):
    pass


def new_chat_member(bot, update):
    pass


def left_chat_member(bot, update):
    pass


