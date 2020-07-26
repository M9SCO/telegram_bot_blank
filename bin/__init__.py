from telegram import Bot
from telegram.ext import Updater

from .config import token
from .sql import connection_to_database

updater: Updater = Updater(token=token, use_context=True)
bot: Bot = updater.bot
cnx, cursor = connection_to_database()
