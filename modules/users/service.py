import os
import modules.users.repository as repository
from modules.profiles.service import ProfilesService

from services.aws.cognito.client import CognitoClient


class UsersService:
    def getPage(limit, page):
        users = repository.getPage(limit, page)
        return users
    

    def getById(userId):
        user = repository.getById(userId)
        return user
    

    def getByUsername(username):
        user = repository.getByUsername(username)
        return user
    

    def create(name, username, password, email):
        CognitoClient.signUp(username, password, email)
        user = repository.create(username, email)
        profile = ProfilesService.create(user.id, name)
        return user, profile