from telegram import Update, Message
from telegram.ext import CallbackContext


def callback_text_messages(update: Update, context: CallbackContext) -> Message:
    message: Message = update.message
    return context.bot.send_message(message.chat.id, text=message.text_html, parse_mode="HTML")

