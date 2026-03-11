import os
from telegram import Bot

TOKEN = os.environ.get("TOKEN", "8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ")
CHAT_ID = os.environ.get("CHAT_ID", "6280782710")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Salam! Hadi message automatic bla ma start user")
