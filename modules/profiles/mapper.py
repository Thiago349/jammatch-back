from modules.profiles.entity import Profile


class ProfilesMapper:
    def entityToDTO(profile: Profile):
        profileDTO = {
            'id': str(profile.id),
            'userId': str(profile.user_id),
            'description': profile.description,
            'profileImage': profile.profile_image,
            'bannerImage': profile.banner_image,
            'createdAt': profile.created_at.isoformat(),
        }

        return profileDTO
