import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🤖 Create a Bot", callback_data="create")],
        [InlineKeyboardButton("💰 Earning Bot", callback_data="earning")],
        [InlineKeyboardButton("📂 My Bots", callback_data="mybots")],
        [InlineKeyboardButton("🆘 Support", callback_data="support")],
    ]

    await update.message.reply_text(
        "🤖 WELCOME TO BOT CREATOR!\n\n"
        "Create and manage your own Telegram bots.\n\n"
        "Choose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "create":
        text = (
            "🤖 CREATE A BOT\n\n"
            "1. Open @BotFather on Telegram.\n"
            "2. Send /newbot and follow the instructions.\n"
            "3. Return here when your bot is ready.\n\n"
            "Bot connection will be added in the next stage."
        )
    elif query.data == "earning":
        text = (
            "💰 EARNING BOT CREATOR\n\n"
            "Referral rewards, tasks, balances and withdrawals "
            "will be configured here.\n\n"
            "This feature is under development."
        )
    elif query.data == "mybots":
        text = "📂 MY BOTS\n\nYour connected bots will appear here."
    else:
        text = "🆘 SUPPORT\n\nContact the platform administrator for help."

    await query.message.reply_text(text)


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()


if __name__ == "__main__":
    main()
