import uuid
from datetime import datetime
from alchemy import db_session
from modules.role_attachments.entity import RoleAttachment


class RoleAttachmentsRepository:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        try:
            roleAttachment: RoleAttachment = db_session.query(RoleAttachment
                ).filter((RoleAttachment.profile_id == profileId) & (RoleAttachment.role_id == roleId) & (RoleAttachment.deleted_at == None)
                    ).first()
            
            if roleAttachment:
                print(roleAttachment.id)
                return None
        
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
    

    def delete(roleAttachmentId: uuid.uuid4, profileId: uuid.uuid4):
        try:
            roleAttachment: RoleAttachment = db_session.query(RoleAttachment
                ).filter((RoleAttachment.id == roleAttachmentId) & (RoleAttachment.deleted_at == None)
                    ).first()

            
            if roleAttachment:
                print(roleAttachment.id)
                if profileId != str(roleAttachment.profile_id):
                    print(profileId, roleAttachment.profile_id)
                    return 403
                roleAttachment.deleted_at = datetime.now()
                db_session.flush()
                db_session.commit()
                return 201
            
            return 404
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return 500 