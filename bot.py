import asyncio
from telegram.ext import Application, CommandHandler

TOKEN = "8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ"
CHAT_ID = 6280782710

async def send_startup_message(application):
    try:
        await application.bot.send_message(
            chat_id=CHAT_ID,
            text="Salam sahbi! البوت رجع يخدم بعد ما حلينا التعارض 🚀"
        )
        print("Startup message wselat")
    except Exception as e:
        print(f"خطأ: {e}")

async def start(update, context):
    await update.message.reply_text("مرحبا أصاحبي! البوت شغال دابا 😏")

async def main():
    application = Application.builder().token(TOKEN).build()

    # أحذف webhook + تجاهل التحديثات القديمة
    await application.bot.delete_webhook(drop_pending_updates=True)
    print("Webhook مسح + drop pending updates")

    application.add_handler(CommandHandler("start", start))
    application.post_init = send_startup_message

    print("البوت غادي يبدأ polling...")
    await application.run_polling(
        allowed_updates=["message", "callback_query"],
        drop_pending_updates=True
    )

if __name__ == "__main__":
    asyncio.run(main())
