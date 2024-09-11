from .service import ProfilesService
from .mapper import ProfilesMapper
from modules.auth.service import AuthService
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Profiles", path="/api/v1/profiles"
)


@api.route("/<profileId>")
class ProfilesController(Resource):
    def put(self, profileId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            profileEntity = ProfilesService.editProfile(profileId)
            profileDTO = ProfilesMapper.entityToDTO(profileEntity)
            return profileDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500

