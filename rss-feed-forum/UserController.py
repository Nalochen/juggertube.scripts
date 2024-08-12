from models import User
from sqlalchemy.orm import Session
from main import engine


def save_new_user_to_database(user_id, user_name):
    existing_user = User.query.filter_by(user_id).first()
    if existing_user:
        if existing_user.name == user_name:
            return
        return f"User {user_name} could not be added to the database, user_id already exists and does not match user_name. Please contact support or try again."

    try:
        with Session(engine) as session:
            new_user = User(id=user_id, name=user_name)
            session.add(new_user)
            session.commit()

            return f"User {user_name} successfully added to database"
    except Exception as e:
        return f"User {user_name} could not be added to the database. Please contact support or try again. {str(e)}"


def get_all_users_from_database():
    return User.query.all()
