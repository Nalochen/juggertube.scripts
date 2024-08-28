import os
import json


filename = 'forum-posts.json'


def get_parent(levels=1):
    current_directory = os.path.dirname(__file__)
    parent_directory = current_directory
    for i in range(0, levels):
        parent_directory = os.path.split(parent_directory)[0]
    file_path = os.path.join(parent_directory, filename)
    return file_path


def read_posts_from_file():
    with open(get_parent()) as json_file:
        data = json.load(json_file)
        return data


def check_if_post_already_was_send(new_post, data):
    for post in data:
        if post["link"] != new_post.link:
            continue
        else:
            return True
    return False


def serialize_posts(post):
    return {
        'link': post.link,
        'author': post.author,
        'title': post.title,
        'category': post.category,
        'published': post.published,
        'updated': post.published
    }


def append_post_to_file(posts):
    new_posts = []
    new_posts_json = []
    if not os.path.isfile(get_parent()):
        for post in posts:
            new_posts_json.append(serialize_posts(post))
        with open(get_parent(), mode='w') as file:
            file.write(json.dumps(new_posts_json, indent=2))
        return posts
    else:
        with open(get_parent()) as file:
            file_posts = json.load(file)
        for post in posts:
            if check_if_post_already_was_send(post, file_posts):
                continue
            else:
                new_posts.append(post)
                file_posts.append(serialize_posts(post))
        with open(get_parent(), mode='w') as file:
            file.write(json.dumps(file_posts, indent=2))
        return new_posts
