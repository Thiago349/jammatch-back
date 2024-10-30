import uuid
from datetime import datetime
from alchemy import db_session
from modules.role_attachments.entity import RoleAttachment
from werkzeug.exceptions import Conflict, NotFound, Forbidden


class RoleAttachmentsRepository:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        try:
            roleAttachment: RoleAttachment = db_session.query(RoleAttachment
                ).filter((RoleAttachment.profile_id == profileId) & (RoleAttachment.role_id == roleId) & (RoleAttachment.deleted_at == None)
                    ).first()
            
            if roleAttachment:
                raise Conflict("Role already exists for this profile")
        
            roleAttachment = RoleAttachment(
                profile_id = profileId,
                role_id = roleId
            )

            db_session.add(roleAttachment)
            db_session.flush()
            db_session.commit()

            return roleAttachment
        
        except Exception as e:
            db_session.rollback()
            raise e
    

    def delete(roleAttachmentId: uuid.uuid4, profileId: uuid.uuid4):
        try:
            roleAttachment: RoleAttachment = db_session.query(RoleAttachment
                ).filter((RoleAttachment.id == roleAttachmentId) & (RoleAttachment.deleted_at == None)
                    ).first()

            
            if roleAttachment:
                if profileId != str(roleAttachment.profile_id):
                    raise Forbidden("Forbidden")
                roleAttachment.deleted_at = datetime.now()
                db_session.flush()
                db_session.commit()
                return roleAttachment.id
            
            raise NotFound(f"No role attachment with '{roleAttachmentId}' id")
            
        except Exception as e:
            db_session.rollback()
            raise e
            