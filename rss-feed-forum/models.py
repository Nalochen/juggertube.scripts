from sqlalchemy import Text, String, DateTime, Integer, Column
from setupDatabase import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"

    def get_id(self):
        return self.id


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(50), nullable=False)
    link = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    content = Column(Text)
    published = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    def __repr__(self):
        return f"Post(id={self.id!r}, author={self.author!r}, link={self.link!r}, title={self.title!r}, " \
               f"content={self.content!r}, published={self.published!r}, updated={self.updated!r}, )"
