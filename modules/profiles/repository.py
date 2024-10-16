import uuid
from alchemy import db_session
from sqlalchemy import and_
from modules.profiles.entity import Profile
from modules.roles.entity import Role
from modules.role_attachments.entity import RoleAttachment
    
class ProfilesRepository:
    def create(mainId: uuid.uuid4, name: str, type: str):
        try:
            profile = Profile(
                main_id = mainId,
                name = name,
                type = type
            )

            db_session.add(profile)
            db_session.flush()
            db_session.commit()

            return profile
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        

    def edit(profileId: uuid.uuid4, payload):
        try:
            profile: Profile = db_session.query(Profile
                ).filter(Profile.id == profileId
                    ).first()

            if profile is None:
                return None
            
            for key in payload:
                if key == 'name':
                    profile.name = payload[key]
                elif key == 'description':
                    profile.description = payload[key]

            db_session.flush()
            db_session.commit()
            
            return profile
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 


    def confirmImageStatus(profileId: uuid.uuid4, imageType: str):
        try:
            profile: Profile = db_session.query(Profile
                ).filter(Profile.id == profileId
                    ).first()

            if imageType == 'photo':
                profile.has_photo = True
            elif imageType == 'banner':
                profile.has_banner = True

            db_session.flush()
            db_session.commit()

            return profile
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        

    def getById(profileId: uuid.uuid4):
        try:
            result = db_session.query(Profile, Role, RoleAttachment
                ).outerjoin(RoleAttachment, (Profile.id == RoleAttachment.profile_id) & (RoleAttachment.deleted_at == None)
                    ).outerjoin(Role, RoleAttachment.role_id == Role.id 
                        ).filter(Profile.id == profileId
                            ).all()
            return result
        
        except Exception as e:
            print(f"ERROR: {e}")
            db_session.rollback()
            return None 
        
