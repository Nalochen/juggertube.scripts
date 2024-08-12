from telegram import Update
from telegram.ext import ContextTypes
from UserController import save_new_user_to_database, get_all_users_from_database


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    save_new_user_to_database(user_id, user_name)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot, please talk to me! " + str(user_id) + ' ' + user_name)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def send_new_posts(context: ContextTypes.DEFAULT_TYPE, posts):
    users = get_all_users_from_database()
    for user in users:
        for post in posts:
            await context.bot.send_message(chat_id=user.id, text=f"{post.author} added a new Post in {post.link}!\n {post.title}\n {post.content}\n published{post.published}")
