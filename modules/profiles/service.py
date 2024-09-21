import uuid
import werkzeug.datastructures

from modules.profiles.repository import ProfilesRepository
from modules.roles.mapper import RolesMapper
from modules.profiles.mapper import ProfilesMapper

from services.aws.s3.client import BucketClient


class ProfilesService:
    def editImage(profileId: uuid.uuid4, file: werkzeug.datastructures.FileStorage, imageType: str):
        bucketName = 'jammatch-bucket'
        objectName = f'{profileId}-{imageType}'

        BucketClient.uploadFile(file, bucketName, objectName)
        profile = ProfilesRepository.confirmImageStatus(profileId, imageType)
        return None if profile is None else ProfilesMapper.entityToDTO(profile)
    

    def edit(profileId: uuid.uuid4, payload: dict):
        profile = ProfilesRepository.edit(profileId, payload)
        return None if profile is None else ProfilesMapper.entityToDTO(profile)
    

    def create(mainId: uuid.uuid4, name: str, type: str):
        profile = ProfilesRepository.create(mainId, name, type)
        return profile
    
    
    def getById(profileId: uuid.uuid4):
        result = ProfilesRepository.getById(profileId)
        if len(result) == 0:
            return None
            
        profile = result[0][0]
        profileDTO = ProfilesMapper.entityToDTO(profile)

        roles = []
        for row in result:
            if row[1] != None:
                roles.append(RolesMapper.entityToDTO(row[1]))

        profileDTO['roles'] = roles

        return profileDTO
    
    