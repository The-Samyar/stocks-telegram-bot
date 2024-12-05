from telegram.ext import Application, CommandHandler
from handlers.commands import start_handler, join_handler, quit_handler
from jobs.alert import schedule_alert
from config import settings


def main():
    print("Running")
    app = Application.builder().token(settings.TELEGRAM_TOKEN).build()

    # Set handlers
    app.add_handlers(
        [
            CommandHandler("start", start_handler),
            CommandHandler("join", join_handler),
            CommandHandler("quit", quit_handler),
        ]
    )

    # Set jobs
    schedule_alert(app, settings.ALERT_INTERVAL)

    app.run_polling()


if __name__ == "__main__":
    main()
