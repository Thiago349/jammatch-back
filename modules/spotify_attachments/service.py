import uuid

from modules.spotify_attachments.repository import SpotifyAttachmentsRepository
from modules.spotify_attachments.mapper import SpotifyAttachmentsMapper


class SpotifyAttachmentsService:
    def create(userId: uuid.uuid4, spotifyId: uuid.uuid4):
        spotifyAttachment = SpotifyAttachmentsRepository.create(userId, spotifyId)
        spotifyAttachmentDTO = SpotifyAttachmentsMapper.entityToDTO(spotifyAttachment)
        return spotifyAttachmentDTO