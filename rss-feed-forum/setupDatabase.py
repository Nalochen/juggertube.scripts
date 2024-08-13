from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

user = 'juggertubeScripts'
password = 'juggertube'
host = 'localhost'
database = 'JuggerTubeScripts'

Base = declarative_base()
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def setup_database():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)





