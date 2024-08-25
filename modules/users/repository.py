from alchemy import db_session
from .entity import User
import uuid


def getUsersPage(limit: int, page: int):
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
    

def getUserById(userId: uuid.uuid4):
    try:
        users: User = db_session.query(User
            ).filter(User.id == userId
                ).first()
        return users
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def createUser(name: str, description: str, username: str, email: str):
    try:
        userEntity = User(
            name = name,
            description = description,
            username = username,
            email = email
        )
        db_session.add(userEntity)
        db_session.flush()
        db_session.commit()

        return userEntity
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 