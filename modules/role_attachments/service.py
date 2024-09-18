import uuid

from modules.role_attachments.repository import RoleAttachmentsRepository


class RoleAttachmentsService:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        profile = RoleAttachmentsRepository.create(profileId, roleId)
        return profile