from modules.role_attachments.entity import RoleAttachment


class RoleAttachmentsMapper:
    def entityToDTO(roleAttachment: RoleAttachment):
        roleAttachmentDTO = {
            'id': str(roleAttachment.id),
            'profileId': str(roleAttachment.profile_id),
            'roleId': str(roleAttachment.role_id),
            'createdAt': roleAttachment.created_at.isoformat(),
        }

        return roleAttachmentDTO
