import asyncio
from telegram.ext import Application, CommandHandler

# Token و Chat ID
TOKEN = "8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ"
CHAT_ID = 6280782710

async def send_startup_message(application):
    try:
        await application.bot.send_message(
            chat_id=CHAT_ID,
            text="Salam sahbi! البوت رجع يخدم بدون مشاكل event loop 🚀"
        )
        print("Startup message وصلت")
    except Exception as e:
        print(f"خطأ في الرسالة: {e}")

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

    # الطريقة الصحيحة في server: شغل run_polling بدون asyncio.run
    await application.initialize()
    await application.start()
    await application.updater.start_polling(
        allowed_updates=["message", "callback_query"],
        drop_pending_updates=True
    )

    # حافظ على الـ loop شغال حتى يوقف
    await asyncio.Event().wait()  # هادا يخلي البوت يبقى شغال إلى الأبد

# شغل الكود بدون asyncio.run إذا كان في event loop موجود
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        # نظف الـ loop عند الخروج
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
