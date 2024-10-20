from services.spotify.endpoints.client import SpotifyClient

from modules.auth.service import AuthService

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
                return {"message": f"Unauthorized"}, 401

            requestArgs = request.args
            if 'userToken' not in requestArgs.keys():
                return {"message": f"Bad Request: 'userToken' required"}, 400
            
            TOKEN = requestArgs['userToken']
            if TOKEN is None:
                return {"message": f"Unauthorized"}, 401

            return SpotifyClient.getSelf(TOKEN), 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/auth")
class RolesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            requestBody = request.json
            if 'code' not in requestBody.keys():
                return {"message": f"Bad Request: 'code' required"}, 400
            
            CODE = requestBody['code']

            return SpotifyClient.authenticate(CODE), 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/auth/refresh")
class RolesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            requestBody = request.json
            if 'refreshToken' not in requestBody.keys():
                return {"message": f"Bad Request: 'refreshToken' required"}, 400
            
            REFRESH_TOKEN = requestBody['refreshToken']

            return SpotifyClient.refresh(REFRESH_TOKEN), 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500