import uuid
import werkzeug.datastructures

from modules.profiles.repository import ProfilesRepository

from services.aws.s3.client import BucketClient

class ProfilesService:
    def editImage(profileId: uuid.uuid4, file: werkzeug.datastructures.FileStorage, imageType: str):
        bucketName = 'jammatch-bucket'
        objectName = f'{profileId}-{imageType}'

        BucketClient.uploadFile(file, bucketName, objectName)
        profile = ProfilesRepository.confirmImageStatus(profileId, imageType)
        return profile
    

    def edit(profileId: uuid.uuid4, payload: dict):
        profile = ProfilesRepository.edit(profileId, payload)
        return profile
    

    def create(mainId: uuid.uuid4, name: str, type: str):
        profile = ProfilesRepository.create(mainId, name, type)
        return profile
    
    
    def getById(profileId: uuid.uuid4):
        result = ProfilesRepository.getById(profileId)
        
        if len(result) == 0:
            return None
            
        profile = result[0][0]
        roles = []
        for row in result:
            if row[1] != None:
                roles.append(row[1])

        return profile, roles
    
    
    def getByMainId(mainId: uuid.uuid4):
        profile = ProfilesRepository.getByMainId(mainId)
        return profile