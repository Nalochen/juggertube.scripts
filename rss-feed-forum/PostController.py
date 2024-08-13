from models import Post
from datetime import datetime
from sqlalchemy.orm import Session
from setupDatabase import engine


def add_new_posts_to_database(posts):
    with Session(engine) as session:
        new_posts = []
        for post in posts:
            existing_post = session.query(Post).filter_by(link=post.link).first()
            if existing_post:
                continue

            published = datetime.strptime(post.published, '%Y-%m-%dT%H:%M:%S+02:00')
            updated = datetime.strptime(post.updated, '%Y-%m-%dT%H:%M:%S+02:00')

            try:
                new_post = Post(author=post.author, link=post.link, title=post.title, content=post.content,
                                updated=updated, published=published, category=post.category)
                session.add(new_post)
                session.commit()
                new_posts.append(post)
            except Exception as e:
                return str(e)

    return new_posts
