from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from backend.models import User, Trip
from backend.database import SessionLocal
from backend.auth import get_password_hash

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

session = SessionLocal()

def start(update: Update, context):
    update.message.reply_text("Привет! Начнем регистрацию?")

def register(update: Update, context):
    message = update.message.text.split()
    if len(message) != 3:
        update.message.reply_text("Формат неверный. Введи /register <имя пользователя> <пароль>")
        return
    username, password = message[1:]
    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    session.add(new_user)
    session.commit()
    update.message.reply_text("Вы успешно зарегистрировались!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
