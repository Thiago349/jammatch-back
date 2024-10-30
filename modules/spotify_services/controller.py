from services.spotify.endpoints.client import SpotifyClient

from modules.auth.service import AuthService
from modules.spotify_services.service import CreatePlaylistService

from werkzeug.exceptions import BadRequest, Forbidden, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Spotify Services", path="/api/v1/spotify-services"
)


@api.route("/self")
class RolesController(Resource):
    def get(self):
        try:
            AuthService.validate(request.headers)

            requestArgs = request.args
            if 'userToken' not in requestArgs.keys():
                raise BadRequest("Bad Request: 'userToken' required")
            
            TOKEN = requestArgs['userToken']

            return SpotifyClient.getSelf(TOKEN), 200
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/auth")
class RolesController(Resource):
    def post(self):
        try:
            AuthService.validate(request.headers)

            requestBody = request.json
            if 'code' not in requestBody.keys():
                raise BadRequest("Bad Request: 'code' required")
            
            CODE = requestBody['code']

            return SpotifyClient.authenticate(CODE), 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/auth/refresh")
class RolesController(Resource):
    def post(self):
        try:
            AuthService.validate(request.headers)

            requestBody = request.json
            if 'refreshToken' not in requestBody.keys():
                raise BadRequest("Bad Request: 'refreshToken' required")
            
            REFRESH_TOKEN = requestBody['refreshToken']

            return SpotifyClient.refresh(REFRESH_TOKEN), 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
        

@api.route("/playlists")
class CreatePlaylist(Resource):
    def post(self):
        try:
            AuthService.validate(request.headers)

            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                raise BadRequest("Bad Request: 'spotifyToken' required")

            spotifyToken = requestBody['spotifyToken']
            userId = requestBody['spotifyUserId']
            playlistName = requestBody['name']
            tracks = requestBody['tracks']

            return CreatePlaylistService.createPlaylist(spotifyToken, userId, playlistName, tracks), 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500