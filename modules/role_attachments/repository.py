import uuid
from alchemy import db_session
from .entity import RoleAttachment


class RoleAttachmentsRepository:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        try:
            profile = RoleAttachment(
                profile_id = profileId,
                role_id = roleId
            )

            db_session.add(profile)
            db_session.flush()
            db_session.commit()

            return profile
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        