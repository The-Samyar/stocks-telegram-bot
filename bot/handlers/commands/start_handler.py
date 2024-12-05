from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""{update.effective_sender.full_name} سلام"""
    text += """\nاین بات بهت این امکان رو میده که زود تر از بقیه از نوسان‌ها و تغییرات دلار با خبر شی."""
    text += """\nبرای دریافت هشدار تغییرات دستور /join رو بزن."""

    await context.bot.send_message(update.effective_chat.id, text=text)
