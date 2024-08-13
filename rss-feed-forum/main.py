import asyncio
import logging

from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler
from telegramBot import start, unknown, send_new_posts
from models import engine, Base
from forumBot import get_forum_posts

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def main():
    Base.metadata.create_all(engine)

    application = ApplicationBuilder().token('7486129110:AAEken4HTskhf5h6YltKI2fVVqXhhiIl3Cs').build()

    start_handler = CommandHandler('start', start)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(start_handler)
    application.add_handler(unknown_handler)

    application.run_polling()


if __name__ == '__main__':
    asyncio.run(main())
