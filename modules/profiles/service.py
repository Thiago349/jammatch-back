import os
import modules.profiles.repository as repository
import uuid


class ProfilesService:
    def edit(profileId: uuid.uuid4):
        profile = repository.edit()
        return profile
    

    def create(userId: uuid.uuid4):
        profile = repository.create(userId)
        return profile
    

    def getByUserId(userId: uuid.uuid4):
        profile = repository.getByUserId(userId)
        return profile