from modules.role_attachments.service import RoleAttachmentsService
from modules.role_attachments.mapper import RoleAttachmentsMapper

from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.users.service import UsersService

from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Role Attachments", path="/api/v1/role-attachments"
)


@api.route("")
class RoleAttachmentsController(Resource):
    def post(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                raise Exception("Unauthorized", 401)

            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['profileId', 'roleId']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise Exception(f"Bad Request: '{', '.join(missingParams)}' required", 400)

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                raise Exception(f"No user with {username} username", 404)

            if userDTO['profile'] and userDTO['profile']['id'] != requestBody['profileId']:
                raise Exception("Forbidden", 403)
            
            roleAttachmentDTO = RoleAttachmentsService.create(requestBody['profileId'], requestBody['roleId'])
            if roleAttachmentDTO is None:
                raise Exception("Role already exists for this profile", 409)
            
            return roleAttachmentDTO, 201
        
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/<roleAttachmentId>")
class RoleAttachmentsController(Resource):
    def delete(self, roleAttachmentId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                raise Exception("Unauthorized", 401)
    
            username = userInformation['Username']

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                raise Exception(f"No user with {username} username", 404)

            roleAttachmentStatus = RoleAttachmentsService.delete(roleAttachmentId, userDTO['profile']['id'])
            print(roleAttachmentStatus)
            if roleAttachmentStatus == 201:
                raise Exception("Succeeded", 201)

            if roleAttachmentStatus == 403: 
                raise Exception("Forbidden", 403)

            if roleAttachmentStatus == 404: 
                raise Exception(f"No role attachment with '{roleAttachmentId}' id", 404)

            raise Exception("Internal Server Error", 500)

        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
