import uuid
from modules.users.repository import UsersRepository
from modules.profiles.service import ProfilesService

from modules.users.mapper import UsersMapper
from modules.roles.mapper import RolesMapper
from modules.profiles.mapper import ProfilesMapper
from modules.spotify_attachments.mapper import SpotifyAttachmentsMapper

from services.aws.cognito.client import CognitoClient


class UsersService:
    def getByUsername(username: str):
        result = UsersRepository.getByUsername(username)
        if len(result) == 0:
            return None

        user = result[0][0]
        profile = result[0][1]
        spotifyAttachment = result[0][2]

        userDTO = UsersMapper.entityToDTO(user)
        if spotifyAttachment != None:
            userDTO['spotify'] = SpotifyAttachmentsMapper.entityToDTO(spotifyAttachment)
        else:
            userDTO['spotify'] = None

        if profile != None:
            userDTO['profile'] = ProfilesMapper.entityToDTO(profile)
            roles = []
            for row in result:
                if row[3] != None:
                    roles.append(RolesMapper.entityToDTO(row[3]))
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