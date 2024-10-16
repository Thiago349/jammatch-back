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
                return {"message": f"Unauthorized"}, 401
            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['profileId', 'roleId']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: '{', '.join(missingParams)}' required"}, 400

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                return f"No user with {username} username", 404

            if userDTO['profile'] and userDTO['profile']['id'] != requestBody['profileId']:
                return {"message": f"Forbidden"}, 403
            
            roleAttachmentDTO = RoleAttachmentsService.create(requestBody['profileId'], requestBody['roleId'])
            if roleAttachmentDTO is None:
                return {"message": f"Role already exists for this profile"}, 409
            return roleAttachmentDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/<roleAttachmentId>")
class RoleAttachmentsController(Resource):
    def delete(self, roleAttachmentId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401
            username = userInformation['Username']

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                return {"message": f"No user with {username} username"}, 404

            roleAttachmentStatus = RoleAttachmentsService.delete(roleAttachmentId, userDTO['profile']['id'])
            print(roleAttachmentStatus)
            if roleAttachmentStatus == 201: 
                return {"message": f"Succeeded"}, 201
            if roleAttachmentStatus == 403: 
                return {"message": f"Forbidden"}, 403
            if roleAttachmentStatus == 404: 
                return {"message": f"No role attachment with '{roleAttachmentId}' id"}, 404
            return {"message": f"Internal Server Error"}, 500
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
