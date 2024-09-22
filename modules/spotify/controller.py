from services.spotify.endpoints.client import SpotifyClient

from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Spotify", path="/api/v1/spotify"
)


@api.route("/self")
class RolesController(Resource):
    def get(self):
        try:
            # userInformation = AuthService.validate(request.headers)
            # if userInformation == None: 
            #     return {"message": f"Unauthorized"}, 401

            requestArgs = request.args
            if ('userToken' in requestArgs.keys()) == False:
                return {"message": f"Bad Request: 'userToken' required"}, 400
            
            TOKEN = requestArgs['userToken']
            if TOKEN is None:
                return {"message": f"Unauthorized"}, 401
            
            headers = {
                "Authorization": f"Bearer {TOKEN}"
            }

            return SpotifyClient.getSelf(headers)
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
