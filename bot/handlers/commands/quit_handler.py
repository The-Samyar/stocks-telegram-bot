from telegram import Update
from telegram.ext import ContextTypes
from redis import Redis


async def quit_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    redis_client = Redis(
        host="localhost",
        port=6380,
    )

    if redis_client.get(update.effective_user.id):
        redis_client.delete(update.effective_user.id)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="از لیست دریافت کننده‌ها با موفقیت حذف شدید",
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="کاربر در لیست دریافت کننده‌ها یافت نشد",
        )
