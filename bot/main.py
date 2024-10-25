import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue
from redis import Redis
import scheduler
from config import TELEGRAM_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""{update.effective_sender.full_name} سلام"""
    text += """\nاین بات بهت این امکان رو میده که زود تر از بقیه از نوسان‌ها و تغییرات دلار با خبر شی."""
    text += """\nبرای دریافت هشدار تغییرات دستور /join رو بزن."""

    await context.bot.send_message(update.effective_chat.id, text=text)


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


async def send_alert(context: ContextTypes.DEFAULT_TYPE):
    print("Sending alert")
    redis_client = Redis(
        host="localhost",
        port=6380,
        decode_responses=True,
    )

    # ----------------- alert sending section -----------------
    chats = redis_client.keys("*")
    for chat in chats:
        print(f"Sending message to {chat}")
        await context.bot.send_message(chat_id=chat, text="hello")


def main():
    print("Running")
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handlers(
        [
            CommandHandler("start", start),
            CommandHandler("join", join_app),
            CommandHandler("quit", quit_app),
        ]
    )

    job_queue: JobQueue = app.job_queue
    job_queue.run_repeating(send_alert, 5)

    app.run_polling()


if __name__ == "__main__":
    main()
