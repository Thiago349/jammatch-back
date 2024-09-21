import uuid
from alchemy import db_session
from .entity import User
from modules.profiles.entity import Profile
from modules.roles.entity import Role
from modules.role_attachments.entity import RoleAttachment


class UsersRepository: 
    def getByUsername(username: str):
        try:
            result = db_session.query(User, Profile, Role
                ).outerjoin(Profile, User.id == Profile.main_id
                    ).outerjoin(RoleAttachment, (Profile.id == RoleAttachment.profile_id) & (RoleAttachment.deleted_at == None)
                        ).outerjoin(Role, RoleAttachment.role_id == Role.id 
                            ).filter(User.username == username
                                ).all()
            return result
        
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