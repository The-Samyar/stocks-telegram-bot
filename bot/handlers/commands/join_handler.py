from telegram import Update
from telegram.ext import ContextTypes
from redis import Redis


async def join_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    redis_client = Redis(
        host="localhost",
        port=6380,
    )
    if redis_client.get(update.effective_user.id):
        text = """\nشما قبلا ثبت شدید."""
        text += """\nاگر میخواید اسمتون از لیست دریافت کننده‌ها حذف شه دستور /quit رو بزنید."""

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )
    else:
        redis_client.set(update.effective_user.id, 1)
        text = """\nبه لیست دریافت کننده‌ها با موفقیت اضافه شدید"""
        text += """\nاگر میخواید اسمتون از لیست دریافت کننده‌ها حذف شه دستور /quit رو بزنید."""

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )
