import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات شما فعال شد ✅")

if name == "__main__":
    app = ApplicationBuilder().token(7682167976:AAGNWMFuhevOus0mexZSRs2ZgFlFUJ-Kufk).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
