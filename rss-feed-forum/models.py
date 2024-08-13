from sqlalchemy import Text, String, DateTime, Integer, Column, create_engine, MetaData, Table
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'juggertubeScripts'
password = 'juggertube'
host = 'localhost'
database = 'JuggerTubeScripts'

Base = declarative_base()


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
    content = Column(Text)
    published = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    def __repr__(self):
        return f"Post(id={self.id!r}, author={self.author!r}, link={self.link!r}, title={self.title!r}, " \
               f"content={self.content!r}, published={self.published!r}, updated={self.updated!r}, )"


engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
