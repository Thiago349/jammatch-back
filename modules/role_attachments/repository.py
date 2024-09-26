import uuid
from alchemy import db_session
from modules.role_attachments.entity import RoleAttachment


class RoleAttachmentsRepository:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        try:
            roleAttachment = RoleAttachment(
                profile_id = profileId,
                role_id = roleId
            )

            db_session.add(roleAttachment)
            db_session.flush()
            db_session.commit()

            return roleAttachment
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        