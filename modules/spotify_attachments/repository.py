import uuid
from alchemy import db_session
from modules.spotify_attachments.entity import SpotifyAttachment


class SpotifyAttachmentsRepository:
    def create(userId: uuid.uuid4, spotifyId: uuid.uuid4):
        try:
            spotifyAttachment = SpotifyAttachment(
                user_id = userId,
                spotify_id = spotifyId
            )

            db_session.add(spotifyAttachment)
            db_session.flush()
            db_session.commit()

            return spotifyAttachment
        
        except Exception as e:
            db_session.rollback()
            raise e
        