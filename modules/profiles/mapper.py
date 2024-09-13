from modules.profiles.entity import Profile


class ProfilesMapper:
    def entityToDTO(profile: Profile):
        profileDTO = {
            'id': str(profile.id),
            'userId': str(profile.user_id),
            'description': profile.description,
            'profileImage': profile.photo_url,
            'bannerImage': profile.banner_url,
            'createdAt': profile.created_at.isoformat(),
            'name': profile.name
        }

        return profileDTO
