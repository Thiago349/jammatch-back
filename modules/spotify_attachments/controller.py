from modules.spotify_attachments.service import SpotifyAttachmentsService
from modules.spotify_attachments.mapper import SpotifyAttachmentsMapper

from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.users.service import UsersService

from werkzeug.exceptions import BadRequest, Forbidden, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Spotify Attachments", path="/api/v1/spotify-attachments"
)


@api.route("")
class SpotifyAttachmentsController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            
            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['userId', 'spotifyId']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")

            userDTO = UsersService.getByUsername(username)
            if userDTO['id'] != requestBody['userId']:
                raise Forbidden("Forbidden")

            spotifyAttachmentDTO = SpotifyAttachmentsService.create(requestBody['userId'], requestBody['spotifyId'])
            return spotifyAttachmentDTO, 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
