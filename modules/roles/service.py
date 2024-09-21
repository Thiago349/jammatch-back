import uuid

from modules.roles.repository import RolesRepository
from modules.roles.mapper import RolesMapper


class RolesService:
    def getByProfileType(profileType: str):
        roles = RolesRepository.getByProfileType(profileType)
        roleDTOs = []
        for role in roles:
            roleDTOs.append(RolesMapper.entityToDTO(role))
        return roleDTOs