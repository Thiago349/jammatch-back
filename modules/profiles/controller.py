from modules.profiles.service import ProfilesService
from modules.profiles.mapper import ProfilesMapper
from modules.auth.service import AuthService

from werkzeug.exceptions import BadRequest, NotFound, Forbidden, Unauthorized, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Profiles", path="/api/v1/profiles"
)


@api.route("")
class ProfilesController(Resource):
    def get(self):
        try:
            limit = int(request.args['limit']) if 'limit' in request.args.keys() else 10
            page = int(request.args['page']) if 'page' in request.args.keys() else 1
            searchText = request.args['searchText'] if 'searchText' in request.args.keys() else None

            AuthService.validate(request.headers)

            profileDTOs = ProfilesService.search(limit, page, searchText)
            return profileDTOs, 200
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/<profileId>")
class ProfilesController(Resource):
    def get(self, profileId):
        try:
            AuthService.validate(request.headers)

            profileDTO = ProfilesService.getById(profileId)           
            return profileDTO, 200

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
        

    def put(self, profileId):
        try:
            AuthService.validate(request.headers)

            profileDTO = ProfilesService.edit(profileId, request.json)           
            return profileDTO, 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/<profileId>/photo")
class ProfilesController(Resource):
    def put(self, profileId):
        try:
            AuthService.validate(request.headers)

            if 'profileImage' not in request.files.keys():
                raise BadRequest(f"Bad Request: 'profileImage' required")
            
            if 'imageType' not in request.form.keys():
                raise BadRequest(f"Bad Request: 'imageType' required")

            if request.form['imageType'] not in ['photo', 'banner']:
                raise BadRequest(f"Bad Request: '{request.form['imageType']}' is not valid for 'imageType'")
            
            profileDTO = ProfilesService.editImage(profileId, request.files['profileImage'], request.form['imageType'])
            return profileDTO, 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500

