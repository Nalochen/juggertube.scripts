from telegram import Update
from telegram.ext import ContextTypes
from userController import save_users_to_json, delete_user_from_json


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_chat.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {user_name}! To register yourself to "
                                                                          f"the Jugger Forum Newsletter either type "
                                                                          f"'/all' or '/qualification'. The first "
                                                                          f"option will send you updates every time a "
                                                                          f"new post was added. The second option only "
                                                                          f"sends you messages when a new post in the "
                                                                          f"Category 'Qualifikation und Liga' from the "
                                                                          f"Region North-West was added. Have fun!")


async def all_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    user_name = update.effective_chat.username
    message = save_users_to_json(user_id, user_name, "all")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def qualification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    user_name = update.effective_chat.username
    message = save_users_to_json(user_id, user_name, "qualification")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    message = delete_user_from_json(user_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
