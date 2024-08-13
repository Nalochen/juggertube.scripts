from UserController import get_all_users_from_database
from telegram import Update
from telegram.ext import ContextTypes
from UserController import save_new_user_to_database


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    user_name = update.effective_chat.username
    save_new_user_to_database(user_id, user_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user_id} {user_name}")


async def send_new_posts(application, posts):
    users = [469350544, 903344761]
    for user_id in users:
        for post in posts:
            if post.category == 'Qualifikation und Liga':
                try:
                    await application.bot.send_message(chat_id=user_id, text=f"{post.author} added a new Post {post.link}!\n{post.title} in {post.category}\npublished: {post.published}")
                except Exception as e:
                    print(str(e))
            else:
                continue
