import uuid
from modules.users.repository import UsersRepository
from modules.profiles.service import ProfilesService

from services.aws.cognito.client import CognitoClient


class UsersService: 
    def getById(userId: uuid.uuid4):
        user, profile = UsersRepository.getById(userId)
        return user, profile
    

    def getByUsername(username: str):
        user, profile = UsersRepository.getByUsername(username)
        return user, profile
    

    def create(name: str, username: str, password: str, email: str):
        CognitoClient.signUp(username, password, email)
        user = UsersRepository.create(username, email)
        profile = ProfilesService.create(user.id, name)
        return user, profile