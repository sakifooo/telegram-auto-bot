import os
import asyncio
from telegram import Bot
from telegram.ext import Application

TOKEN = os.getenv("8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ")
CHAT_ID = os.getenv("6280782710")  # أو حدديه مباشرة إذا ثابت

async def send_welcome():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Salam! Hadi message automatic bla ma start user")

# شغلي الدالة async
asyncio.run(send_welcome())

# بعدين ابدأ polling (إذا بغيتي البوت يبقى شغال)
application = Application.builder().token(TOKEN).build()
# أضيفي handlers ديالك هنا...
application.run_polling()
