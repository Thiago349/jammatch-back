import os
import modules.users.repository as repository


class UsersService:
    def getUsers(limit, page):
        users = repository.getUsersPage(limit, page)
        return {"status_code": 201, "data": users}
    

    def getUserById(userId):
        user = repository.getUserById(userId)
        return {"status_code": 201, "data": user}
    

    def createUser(name, description, username, email):
        user = repository.createUser(name, description, username, email)
        return {"status_code": 201, "data": user}