import uuid

from modules.role_attachments.repository import RoleAttachmentsRepository
from modules.role_attachments.mapper import RoleAttachmentsMapper


class RoleAttachmentsService:
    def create(profileId: uuid.uuid4, roleId: uuid.uuid4):
        roleAttachment = RoleAttachmentsRepository.create(profileId, roleId)
        roleAttachmentDTO = RoleAttachmentsMapper.entityToDTO(roleAttachment)
        return roleAttachmentDTO
    

    def delete(roleAttachmentId: uuid.uuid4, profileId: uuid.uuid4):
        roleAttachmentId = RoleAttachmentsRepository.delete(roleAttachmentId, profileId)
        return roleAttachmentId