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
            
            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                return {"message": "Bad Request: 'spotifyToken' required"}, 400

            spotifyToken = requestBody['spotifyToken']
            
            return LabServicesService.generateRamdomPlaylist(spotifyToken), 201

        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
    
             

            

    
