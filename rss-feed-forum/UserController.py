from models import User, engine
from sqlalchemy.orm import Session


def save_new_user_to_database(user_id, user_name):
    with Session(engine) as session:
        existing_user = session.query(User).filter_by(id=user_id).first()
        if existing_user:
            if existing_user.name == user_name:
                print('User already added')
            else:
                print(f"User {user_name} could not be added to the database, user_id already exists and does not match user_name. Please contact support or try again.")
        else:
            try:
                new_user = User(id=user_id, name=user_name)
                session.add(new_user)
                session.commit()

                print(f"User {user_name} successfully added to database")
            except Exception as e:
                print(f"User {user_name} could not be added to the database. Please contact support or try again. {str(e)}")


def get_all_users_from_database():
    with Session(engine) as session:
        return session.query(User).all()
