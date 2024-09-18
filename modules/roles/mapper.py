from modules.roles.entity import Role


class RolesMapper:
    def entityToDTO(role: Role):
        roleDTO = {
            'id': str(role.id),
            'label': str(role.label),
            'roleId': str(role.profile_type)
        }

        return roleDTO
