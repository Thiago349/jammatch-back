from modules.spotify_attachments.entity import SpotifyAttachment


class SpotifyAttachmentsMapper:
    def entityToDTO(spotifyAttachment: SpotifyAttachment):
        spotifyAttachmentDTO = {
            'id': str(spotifyAttachment.id),
            'userId': str(spotifyAttachment.user_id),
            'spotifyId': str(spotifyAttachment.spotify_id),
            'createdAt': spotifyAttachment.created_at.isoformat(),
        }

        return spotifyAttachmentDTO
