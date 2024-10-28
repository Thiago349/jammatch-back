from modules.spotify_attachments.service import SpotifyAttachmentsService
from modules.spotify_attachments.mapper import SpotifyAttachmentsMapper

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
                raise Exception("Unauthorized", 401)
            
            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['userId', 'spotifyId']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise Exception(f"Bad Request: '{', '.join(missingParams)}' required", 400)

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                raise Exception(f"No user with {username} username", 404)

            if userDTO['id'] != requestBody['userId']:
                raise Exception("Forbidden", 403)

            spotifyAttachmentDTO = SpotifyAttachmentsService.create(requestBody['userId'], requestBody['spotifyId'])
            return spotifyAttachmentDTO, 201
        
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
