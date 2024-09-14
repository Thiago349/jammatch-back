from .service import ProfilesService
from .mapper import ProfilesMapper
from modules.auth.service import AuthService
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Profiles", path="/api/v1/profiles"
)


@api.route("/<profileId>/photo")
class ProfilesController(Resource):
    def put(self, profileId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            if ('profileImage' in request.files.keys()) == False:
                return {"message": f"Bad Request: 'profileImage' required"}, 400
            
            if ('imageType' in request.form.keys()) == False:
                return {"message": f"Bad Request: 'imageType' required"}, 400

            if (request.form['imageType'] in ['photo', 'banner']) == False:
                return {"message": f"Bad Request: '{request.form['imageType']}' is not valid for 'imageType'"}, 400
            
            profileEntity = ProfilesService.editImage(profileId, request.files['profileImage'], request.form['imageType'])
            profileDTO = ProfilesMapper.entityToDTO(profileEntity)
            return profileDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500

