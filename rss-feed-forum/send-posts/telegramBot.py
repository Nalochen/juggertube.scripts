from userController import read_users_from_json


async def send_new_posts(application, posts):
    users = read_users_from_json()
    for user in users:
        for post in posts:
            if user["information"] == "qualification" and post.category == 'Qualifikation und Liga':
                try:
                    await application.bot.send_message(chat_id=user["userId"], text=f"{post.author} added a new Post "
                                                                                    f"{post.link}!\n{post.title} in "
                                                                                    f"{post.category}\npublished: "
                                                                                    f"{post.published}")
                except Exception as e:
                    print(str(e))
            elif user["information"] == "all":
                try:
                    await application.bot.send_message(chat_id=user["userId"], text=f"{post.author} added a new Post "
                                                                                    f"{post.link}!\n{post.title} in "
                                                                                    f"{post.category}\npublished: "
                                                                                    f"{post.published}")
                except Exception as e:
                    print(str(e))
