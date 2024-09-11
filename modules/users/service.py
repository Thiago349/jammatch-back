import os
import modules.users.repository as repository
from modules.profiles.service import ProfilesService

from services.cognito.client import CognitoClient


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
        user = repository.create(name, username, email)
        profile = ProfilesService.create(user.id)
        return user, profile