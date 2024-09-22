import uuid
from modules.users.repository import UsersRepository
from modules.profiles.service import ProfilesService

from modules.users.mapper import UsersMapper
from modules.roles.mapper import RolesMapper
from modules.profiles.mapper import ProfilesMapper

from services.aws.cognito.client import CognitoClient


class UsersService:
    def getByUsername(username: str):
        result = UsersRepository.getByUsername(username)
        if len(result) == 0:
            return None

        user = result[0][0]
        profile = result[0][1]

        userDTO = UsersMapper.entityToDTO(user)
        if profile != None:
            userDTO['profile'] = ProfilesMapper.entityToDTO(profile)
            roles = []
            for row in result:
                if row[2] != None:
                    roles.append(RolesMapper.entityToDTO(row[2]))
            userDTO['profile']['roles'] = roles
        else:
            userDTO['profile'] = None

        return userDTO
    

    def create(name: str, username: str, password: str, email: str):
        CognitoClient.signUp(username, password, email)
        user = UsersRepository.create(username, email)
        profile = ProfilesService.create(user.id, name, "USER")

        userDTO = UsersMapper.entityToDTO(user)
        profileDTO = ProfilesMapper.entityToDTO(profile)
        userDTO['profile'] = profileDTO
        return userDTO