import logging

from telegram.ext import ApplicationBuilder, CommandHandler
from telegramBot import start
from setupDatabase import setup_database


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    setup_database()
    application = ApplicationBuilder().token('7486129110:AAEken4HTskhf5h6YltKI2fVVqXhhiIl3Cs').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
