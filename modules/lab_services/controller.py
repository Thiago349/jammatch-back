import random
import requests

from werkzeug.exceptions import BadRequest, Unauthorized, HTTPException
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
            AuthService.validate(request.headers)
            
            limit = int(request.json['limit']) if 'limit' in request.json.keys() else 10
            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                raise BadRequest("Bad Request: 'spotifyToken' required")

            spotifyToken = requestBody['spotifyToken']

            return LabServicesService.generateRandomPlaylist(spotifyToken, limit), 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
    
             
@api.route("/custom")
class LabServicesController(Resource):
    def post(self):
        try:
            AuthService.validate(request.headers)
            
            limit = int(request.json['limit']) if 'limit' in request.json.keys() else 10
            playlistName = request.json['playlistName'] if 'playlistName' in request.json.keys() else None
            requestBody = request.json
            paramsToCheck = ['spotifyToken', 'params']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")

            spotifyToken = requestBody['spotifyToken']
            customParams = requestBody['params']

            return LabServicesService.generateCustomPlaylist(spotifyToken, customParams, playlistName, limit), 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500