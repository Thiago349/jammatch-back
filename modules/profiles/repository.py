import uuid
from alchemy import db_session
from .entity import Profile
    

def create(userId: uuid.uuid4, name: str):
    try:
        profile = Profile(
            user_id = userId,
            name = name
        )
        db_session.add(profile)
        db_session.flush()
        db_session.commit()

        return profile
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def edit(profileId: uuid.uuid4):
    try:
        profile = Profile(
            id = profileId
        )
        db_session.add(profile)
        db_session.flush()
        db_session.commit()

        return profile
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def getByUserId(userId: uuid.uuid4):
    try:
        profile: Profile = db_session.query(Profile
            ).filter(Profile.user_id == userId
                ).first()
        return profile
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 