import asyncio
import logging

from telegram.ext import ApplicationBuilder
from telegramBot import send_new_posts
from forumBot import get_forum_posts
from PostController import add_new_posts_to_database
from setupDatabase import setup_database

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def main():
    setup_database()
    application = ApplicationBuilder().token('7486129110:AAEken4HTskhf5h6YltKI2fVVqXhhiIl3Cs').build()

    await application.initialize()

    new_posts = get_forum_posts()
    await send_new_posts(application, add_new_posts_to_database(new_posts))

    polling_task = asyncio.create_task(application.start())

    try:
        # Keep the application running
        await application.updater.start_polling()
    finally:
        # Stop the application gracefully
        await application.stop()
        await polling_task


if __name__ == '__main__':
    asyncio.run(main())
