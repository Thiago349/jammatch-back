from modules.profiles.entity import Profile


class ProfilesMapper:
    def entityToDTO(profile: Profile):
        profileDTO = {
            'id': str(profile.id),
            'userId': str(profile.user_id),
            'description': profile.description,
            'hasPhoto': profile.has_photo,
            'hasBanner': profile.has_banner,
            'createdAt': profile.created_at.isoformat(),
            'name': profile.name
        }

        return profileDTO
