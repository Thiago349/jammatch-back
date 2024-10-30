import uuid
from alchemy import db_session
from modules.roles.entity import Role
    

class RolesRepository:
    def getByProfileType(type: str):
        try:
            roles: Role = db_session.query(Role
                ).order_by(Role.label.asc()
                    ).filter(Role.profile_type == type
                        ).all()
            return roles
        
        except Exception as e:
            db_session.rollback()
            raise e
    