import xml.etree.ElementTree as ET
import requests
from post import Post


def get_forum_posts():
    response = requests.get('https://forum.jugger.org/app.php/feed')
    forum_xml = response.text

    tree = ET.fromstring(forum_xml)

    last_entries = []

    for entry in tree.findall('{http://www.w3.org/2005/Atom}entry'):
        author = entry.find('{http://www.w3.org/2005/Atom}author')
        author_name = author.find('{http://www.w3.org/2005/Atom}name')
        updated = entry.find('{http://www.w3.org/2005/Atom}updated')
        published = entry.find('{http://www.w3.org/2005/Atom}published')
        post_id = entry.find('{http://www.w3.org/2005/Atom}id')
        category_title = entry.find('{http://www.w3.org/2005/Atom}title')
        category_title_list = category_title.text.split(' • ')

        category = category_title_list[0]
        title = category_title_list[1]

        current_post = Post(link=post_id.text, author=author_name.text, title=title, published=published.text,
                            updated=updated.text, category=category)
        last_entries.append(current_post)

    return last_entries


if __name__ == '__main__':
    get_forum_posts()
