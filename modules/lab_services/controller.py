import random
import requests
from flask_restx import Namespace, Resource
from flask import request
from services.spotify.endpoints.client import SpotifyClient
from modules.auth.service import AuthService
from modules.lab_services.service import LabServicesService


api = Namespace(
    "Lab Services", path="/api/v1/lab-services"
)


@api.route("/random")
class LabServicesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation is None:
                return {"message": "Unauthorized"}, 401
            
            limit = int(request.json['limit']) if 'limit' in request.json.keys() else 10
            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                return {"message": "Bad Request: 'spotifyToken' required"}, 400

            spotifyToken = requestBody['spotifyToken']

            return LabServicesService.generateRandomPlaylist(spotifyToken, limit), 201

        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
    
             
@api.route("/custom")
class LabServicesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation is None:
                return {"message": "Unauthorized"}, 401
            
            limit = int(request.json['limit']) if 'limit' in request.json.keys() else 10
            playlistName = request.json['playlistName'] if 'playlistName' in request.json.keys() else None
            requestBody = request.json
            paramsToCheck = ['spotifyToken', 'params']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: '{', '.join(missingParams)}' required"}, 400

            spotifyToken = requestBody['spotifyToken']
            customParams = requestBody['params']

            return LabServicesService.generateCustomPlaylist(spotifyToken, customParams, playlistName, limit), 201

        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500