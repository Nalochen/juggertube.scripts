from telegram.ext import ApplicationBuilder, CommandHandler
from telegramBot import all_posts, qualification, start, unsubscribe

if __name__ == '__main__':
    application = ApplicationBuilder().token('7486129110:AAEken4HTskhf5h6YltKI2fVVqXhhiIl3Cs').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    all_handler = CommandHandler('all', all_posts)
    application.add_handler(all_handler)
    qualification_handler = CommandHandler('qualification', qualification)
    application.add_handler(all_handler)
    unsubscribe_handler = CommandHandler('unsubscribe', unsubscribe)
    application.add_handler(unsubscribe_handler)

    application.run_polling()
