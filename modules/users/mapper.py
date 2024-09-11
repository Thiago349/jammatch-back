from modules.users.entity import User


class UsersMapper:
    def entityToDTO(user: User):
        userDTO = {
            'id': str(user.id),
            'name': str(user.name),
            'email': user.email,
            'username': user.username,
        }
            
        return userDTO
