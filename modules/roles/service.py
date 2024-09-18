import uuid

from modules.roles.repository import RolesRepository


class RolesService:
    def getByProfileType(profileType: str):
        profile = RolesRepository.getByProfileType(profileType)
        return profile