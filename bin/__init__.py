from telegram import Bot
from telegram.ext import Updater

from .config import token


updater: Updater = Updater(token=token, use_context=True)
bot: Bot = updater.bot
