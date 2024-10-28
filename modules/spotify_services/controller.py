from services.spotify.endpoints.client import SpotifyClient

from modules.auth.service import AuthService
from modules.spotify_services.service import CreatePlaylistService

from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Spotify Services", path="/api/v1/spotify-services"
)


@api.route("/self")
class RolesController(Resource):
    def get(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                raise Exception("Unauthorized", 401)

            requestArgs = request.args
            if 'userToken' not in requestArgs.keys():
                raise Exception("Bad Request: 'userToken' required", 400)
            
            TOKEN = requestArgs['userToken']

            return SpotifyClient.getSelf(TOKEN), 200
        
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error"}, 500


@api.route("/auth")
class RolesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                raise Exception("Unauthorized", 401)

            requestBody = request.json
            if 'code' not in requestBody.keys():
                raise Exception("Bad Request: 'code' required", 400)
            
            CODE = requestBody['code']

            return SpotifyClient.authenticate(CODE), 201
        
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error"}, 500


@api.route("/auth/refresh")
class RolesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None:
                raise Exception("Unauthorized", 401)

            requestBody = request.json
            if 'refreshToken' not in requestBody.keys():
                raise Exception("Bad Request: 'refreshToken' required", 400)
            
            REFRESH_TOKEN = requestBody['refreshToken']

            return SpotifyClient.refresh(REFRESH_TOKEN), 201
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error"}, 500
        

@api.route("/playlists")
class CreatePlaylist(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation is None:
                raise Exception("Unauthorized", 401)
            
            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                raise Exception("Bad Request: 'spotifyToken' required", 400)

            spotifyToken = requestBody['spotifyToken']

            userId = requestBody['spotifyUserId']

            playlistName = requestBody['name']

            tracks = requestBody['tracks']

            return CreatePlaylistService.createPlaylist(spotifyToken, userId, playlistName, tracks), 201

        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
                
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error"}, 500