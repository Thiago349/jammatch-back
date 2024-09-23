from .service import SpotifyAttachmentsService
from .mapper import SpotifyAttachmentsMapper

from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.users.service import UsersService

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
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401
            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['userId', 'spotifyId']
            missingParams = []
            for param in paramsToCheck:
                if (param in requestBody.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: '{', '.join(missingParams)}' required"}, 400

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                return f"No user with {username} username", 404

            if userDTO['id'] != requestBody['userId']:
                return {"message": f"Forbidden"}, 403

            spotifyAttachmentDTO = SpotifyAttachmentsService.create(requestBody['userId'], requestBody['spotifyId'])
            return spotifyAttachmentDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
