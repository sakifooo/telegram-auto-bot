import os
import asyncio
from telegram import Bot
from telegram.ext import Application, CommandHandler

# قراءة المتغيرات من البيئة (Koyeb / Railway / أي منصة)
TOKEN = os.getenv("8636119556:AAHN2lW72qjFB1nUdYzpAPFdLmeNtJvBcGQ")
CHAT_ID = os.getenv("6280782710")  # إذا ما حددتيه في env vars → غادي يفشل، أو حدديه ثابت هنا

if not TOKEN:
    print("خطأ: TELEGRAM_TOKEN مش موجود في المتغيرات البيئية!")
    exit(1)

# إذا ما عندك CHAT_ID في env vars، حدديه هنا (مثال شخصي أو group)
# CHAT_ID = "123456789"   # غيريه برقمك أو -100xxxxxxxxxx للـ group

async def send_startup_message(application: Application) -> None:
    """
    دالة كاتبعت رسالة تلقائية لما البوت يبدأ (startup message)
    """
    try:
        await application.bot.send_message(
            chat_id=CHAT_ID,
            text="Salam! البوت بدا يخدم دلوقت 🚀\nHadi رسالة تلقائية لما يشتغل."
        )
        print("Startup message sent successfully!")
    except Exception as e:
        print(f"خطأ في إرسال الرسالة التلقائية: {e}")

async def start(update, context):
    """أمر /start بسيط"""
    await update.message.reply_text("مرحبا! أنا البوت ديالك. كيفاش نقدر نساعدك؟")

def main():
    # بناء التطبيق
    application = Application.builder().token(TOKEN).build()

    # أضف handler للأمر /start
    application.add_handler(CommandHandler("start", start))

    # أضف دالة post_init باش تبعت الرسالة التلقائية لما يبدأ البوت
    application.post_init = send_startup_message

    print("البوت غادي يبدأ polling...")
    # شغل long polling (الطريقة الأسهل والأكثر استقراراً على Koyeb/Railway)
    application.run_polling(
        allowed_updates=["message", "callback_query"],  # حدد التحديثات اللي تحتاجيها
        drop_pending_updates=True  # تجاهل الرسائل القديمة لما يرجع يشتغل
    )

if __name__ == "__main__":
    main()
