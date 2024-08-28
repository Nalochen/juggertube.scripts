import json
import os

from user import User

filename = "telegramIds.json"


def get_parent(levels=1):
    current_directory = os.path.dirname(__file__)
    parent_directory = current_directory
    for i in range(0, levels):
        parent_directory = os.path.split(parent_directory)[0]
    file_path = os.path.join(parent_directory, filename)
    return file_path


def check_if_user_already_exists(user_to_search, all_users):
    for user in all_users:
        if user["userId"] != user_to_search.user_id:
            continue
        else:
            return True
    return False


def serialize_user(user):
    return {
        "userId": user.user_id,
        "userName": user.user_name,
        "information": user.information
    }


def save_users_to_json(user_id, user_name, information):
    new_users = []
    new_user = User(user_id=user_id, user_name=user_name, information=information)
    if not os.path.isfile(get_parent()):
        with open(get_parent(), 'w') as file:
            new_users.append(serialize_user(new_user))
            file.write(json.dumps(new_users, indent=2))
    else:
        with open(get_parent()) as file:
            file_users = json.load(file)
            if check_if_user_already_exists(new_user, file_users):
                return "user already subscribed to newsletter"
            else:
                file_users.append(serialize_user(new_user))
        with open(get_parent(), 'w') as file:
            file.write(json.dumps(file_users, indent=2))

    if information == "qualification":
        return (f"Congratulations! You just subscribed to the Jugger Forum Newsletter and get a message every time a "
                f"new post in the Category 'Qualifiaktion und Liga' was added")
    else:
        return (
            f"Congratulations! You just subscribed to the Jugger Forum Newsletter and get a message every time a new "
            f"post was added")


def delete_user_from_json(user_id):
    if not os.path.isfile(get_parent()):
        return "user does not exist on database"
    with open(get_parent()) as file:
        file_users = json.load(file)
        for user in file_users:
            if user.user_id == user_id:
                del file_users[user]
                return f"user {user.user_name} unsubscribed"
            else:
                return f"user {user.user_name} not found"
