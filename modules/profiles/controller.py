from modules.profiles.service import ProfilesService
from modules.profiles.mapper import ProfilesMapper
from modules.auth.service import AuthService
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Profiles", path="/api/v1/profiles"
)


@api.route("/<profileId>")
class ProfilesController(Resource):
    def get(self, profileId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            profileDTO = ProfilesService.getById(profileId)
            if profileDTO == None:
                return f"Not Found: No profile with '{profileId}' id", 404
            
            return profileDTO, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
        

    def put(self, profileId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            profileDTO = ProfilesService.edit(profileId, request.json)
            if profileDTO == None:
                return f"Not Found: No profile with '{profileId}' id", 404
            
            return profileDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/<profileId>/photo")
class ProfilesController(Resource):
    def put(self, profileId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            if 'profileImage' not in request.files.keys():
                return {"message": f"Bad Request: 'profileImage' required"}, 400
            
            if 'imageType' not in request.form.keys():
                return {"message": f"Bad Request: 'imageType' required"}, 400

            if request.form['imageType'] not in ['photo', 'banner']:
                return {"message": f"Bad Request: '{request.form['imageType']}' is not valid for 'imageType'"}, 400
            
            profileDTO = ProfilesService.editImage(profileId, request.files['profileImage'], request.form['imageType'])
            if profileDTO == None:
                return f"Not Found: No profile with '{profileId}' id", 404
            
            return profileDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500

