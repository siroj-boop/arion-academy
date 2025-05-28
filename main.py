from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔒 Вставь сюда свой токен БЕЗОПАСНО
TOKEN = "8009596428:AAEGYJild4leGK688ceb482CHR1fb82Lr7U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            text="Arion Academy",
            web_app=WebAppInfo(url="https://arion-academy.onrender.com/webapp")
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет 👋 Добро пожаловать в ARION! Нажми кнопку ниже, чтобы открыть WebApp:", reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
