import uuid
from alchemy import db_session
from .entity import Profile
    

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
    

def getByMainId(mainId: uuid.uuid4):
    try:
        profile: Profile = db_session.query(Profile
            ).filter(Profile.main_id == mainId
                ).first()
        return profile
    
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 