import os
import modules.users.repository as repository


class UsersService:
    def getUsers(limit, page):
        users = repository.getUsersPage(limit, page)
        return users
    

    def getUserById(userId):
        user = repository.getUserById(userId)
        return user
    

    def createUser(name, description, username, password, email):
        user = repository.createUser(name, description, username, password, email)
        return user