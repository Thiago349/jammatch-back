from services.cognito.client import CognitoClient
import uuid
from alchemy import db_session
from .entity import User


def getPage(limit: int, page: int):
    try:
        users: User = db_session.query(User
            ).order_by(User.created_at.desc()
                ).limit(limit
                    ).offset(limit * (page - 1)
                        ).all()
        return users
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None
    

def getById(userId: uuid.uuid4):
    try:
        user: User = db_session.query(User
            ).filter(User.id == userId
                ).first()
        return user
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def getByUsername(username: str):
    try:
        user: User = db_session.query(User
            ).filter(User.username == username
                ).first()
        return user
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def create(name: str, username: str, email: str):
    try:
        user = User(
            name = name,
            username = username,
            email = email
        )
        db_session.add(user)
        db_session.flush()
        db_session.commit()

        return user
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 