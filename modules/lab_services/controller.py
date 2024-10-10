from services.spotify.endpoints.client import SpotifyClient

from modules.auth.service import AuthService

from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Lab Services", path="/api/v1/lab-services"
)


@api.route("/random")
class RolesController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            requestBody = request.json
            if 'spotifyToken' not in requestBody.keys():
                return {"message": f"Bad Request: 'spotifyToken' required"}, 400
            
            return {"message": f"Succeeded!"}
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500