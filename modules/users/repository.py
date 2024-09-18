import uuid
from alchemy import db_session
from .entity import User
from modules.profiles.entity import Profile


class UsersRepository: 
    def getById(userId: uuid.uuid4):
        try:
            user, profile = db_session.query(User, Profile
                ).outerjoin(Profile, User.id == Profile.main_id
                    ).filter(User.id == userId
                        ).first()
            return user, profile
            
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        

    def getByUsername(username: str):
        try:
            user, profile = db_session.query(User, Profile
                ).outerjoin(Profile, User.id == Profile.main_id
                    ).filter(User.username == username
                        ).first()
            return user, profile
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        

    def create(username: str, email: str):
        try:
            user = User(
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