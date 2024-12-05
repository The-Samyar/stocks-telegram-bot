from telegram.ext import ContextTypes, JobQueue
from redis import Redis


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


def schedule_alert(app, interval):
    """
    Schedules the `send_alert` job.
    """

    job_queue: JobQueue = app.job_queue
    job_queue.run_repeating(send_alert, interval)
