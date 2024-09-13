import uuid
import werkzeug.datastructures

import modules.profiles.repository as repository

from services.aws.s3.client import BucketClient

class ProfilesService:
    def editPhoto(profileId: uuid.uuid4, file: werkzeug.datastructures.FileStorage):
        bucketName = 'jammatch-bucket'
        objectName = f'{profileId}-photo'

        BucketClient.uploadFile(file, bucketName, objectName)
        # profile = repository.editPhoto(profileId, file)
        return 200
    

    def create(userId: uuid.uuid4, name: str):
        profile = repository.create(userId, name)
        return profile
    

    def getByUserId(userId: uuid.uuid4):
        profile = repository.getByUserId(userId)
        return profile