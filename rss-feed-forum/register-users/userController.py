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


def check_if_user_already_exists(new_user, all_users):
    for user in all_users:
        if user["userId"] != new_user.user_id:
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
    if not os.path.isfile(filename):
        with open(get_parent(), 'w') as file:
            new_users.append(serialize_user(new_user))
            file.write(json.dumps(new_users, indent=2))
    else:
        with open(get_parent()) as file:
            file_users = json.load(file)
            if check_if_user_already_exists(new_user, file_users):
                return
            else:
                file_users.append(serialize_user(new_user))
        with open(get_parent(), 'w') as file:
            file.write(json.dumps(file_users, indent=2))
