import uuid
from alchemy import db_session
from sqlalchemy import and_
from modules.profiles.entity import Profile
from modules.roles.entity import Role
from modules.role_attachments.entity import RoleAttachment
from werkzeug.exceptions import NotFound


class ProfilesRepository:
    def search(limit: int, page: int, searchText = None):
        try:
            offset = (page - 1) * limit
            result = db_session.query(Profile
                ).offset(offset
                    ).limit(limit
                        ).all()
            print(result)
            return result
        
        except Exception as e:
            db_session.rollback()
            raise e


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
            db_session.rollback()
            raise e
        

    def edit(profileId: uuid.uuid4, payload):
        try:
            profile: Profile = db_session.query(Profile
                ).filter(Profile.id == profileId
                    ).first()

            if profile is None:
                raise NotFound(f"Not Found: No profile with '{profileId}' id")
            
            for key in payload:
                if key == 'name':
                    profile.name = payload[key]
                elif key == 'description':
                    profile.description = payload[key]

            db_session.flush()
            db_session.commit()
            
            return profile
        
        except Exception as e:
            db_session.rollback()
            raise e


    def confirmImageStatus(profileId: uuid.uuid4, imageType: str):
        try:
            profile: Profile = db_session.query(Profile
                ).filter(Profile.id == profileId
                    ).first()
            
            if profile is None:
                raise NotFound(f"Not Found: No profile with '{profileId}' id")
            
            if imageType == 'photo':
                profile.has_photo = True
            elif imageType == 'banner':
                profile.has_banner = True

            db_session.flush()
            db_session.commit()

            return profile
        
        except Exception as e:
            db_session.rollback()
            raise e
        

    def getById(profileId: uuid.uuid4):
        try:
            result = db_session.query(Profile, Role, RoleAttachment
                ).outerjoin(RoleAttachment, (Profile.id == RoleAttachment.profile_id) & (RoleAttachment.deleted_at == None)
                    ).outerjoin(Role, RoleAttachment.role_id == Role.id 
                        ).filter(Profile.id == profileId
                            ).all()
            return result
        
        except Exception as e:
            db_session.rollback()
            raise e
        
