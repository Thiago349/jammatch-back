from modules.users.entity import User


class UsersMapper:
    def userEntityToDTO(user: User):
        userDTO = {
            'id': str(user.id),
            'name': str(user.name),
            'email': str(user.email),
            'username': str(user.username),
            'createdAt': user.created_at.isoformat(),
        }

        if user.description:
            userDTO['description'] = str(user.description)
        else:
            userDTO[['description']] = user.description

        if user.deleted_at:
            userDTO['deletedAt'] = user.deleted_at.isoformat()
        else:
            userDTO['deletedAt'] = user.deleted_at
        return userDTO
