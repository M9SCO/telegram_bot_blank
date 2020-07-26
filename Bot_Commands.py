from telegram import Update, Message
from telegram.ext import CallbackContext

from bin.config import text_start


def start(update: Update, context: CallbackContext) -> Message:
    return context.bot.send_message(update.message.chat.id, text_start)
