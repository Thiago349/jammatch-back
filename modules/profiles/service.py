import uuid
import werkzeug.datastructures

import modules.profiles.repository as repository

from services.aws.s3.client import BucketClient

class ProfilesService:
    def editImage(profileId: uuid.uuid4, file: werkzeug.datastructures.FileStorage, imageType: str):
        bucketName = 'jammatch-bucket'
        objectName = f'{profileId}-{imageType}'

        BucketClient.uploadFile(file, bucketName, objectName)
        profile = repository.confirmImageStatus(profileId, imageType)
        return profile
    

    def edit(profileId: uuid.uuid4, payload: dict):
        profile = repository.edit(profileId, payload)
        return profile
    

    def create(mainId: uuid.uuid4, name: str, type: str):
        profile = repository.create(mainId, name, type)
        return profile
    

    def getByMainId(mainId: uuid.uuid4):
        profile = repository.getByMainId(mainId)
        return profile