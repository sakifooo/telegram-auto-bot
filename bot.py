import asyncio
from telegram.ext import Application, CommandHandler

# Token w Chat ID li 3titi
TOKEN = "8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ"
CHAT_ID = 6280782710

# رسالة تلقائية كيبدأ البوت (startup message)
async def send_startup_message(application):
    try:
        await application.bot.send_message(
            chat_id=CHAT_ID,
            text="Salam sahbi! البوت بدا يخدم دلوقت 🚀\nHadi رسالة تلقائية bach n3rfk bli khddam."
        )
        print("Startup message wselat mzyan!")
    except Exception as e:
        print(f"مشكل ف الرسالة التلقائية: {e}")

# أمر /start بسيط
async def start(update, context):
    await update.message.reply_text(
        "مرحبا أصاحبي! أنا هنا باش نساعدك.\nشنو بغيتي ندير ليك دابا؟ 😏"
    )

def main():
    # بناء البوت
    application = Application.builder().token(TOKEN).build()

    # أضف أمر /start
    application.add_handler(CommandHandler("start", start))

    # باش يبعت الرسالة التلقائية كيبدأ
    application.post_init = send_startup_message

    print("البوت غادي يبدأ polling...")
    print(f"Chat ID li ghadi nshddo: {CHAT_ID}")
# قبل application.run_polling()
await application.bot.delete_webhook(drop_pending_updates=True)
print("Webhook تم مسحو + pending updates تم تجاهلهم")
    # Long polling (الأسهل و الأكثر استقرار على Koyeb)
    application.run_polling(
        allowed_updates=["message", "callback_query"],
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
