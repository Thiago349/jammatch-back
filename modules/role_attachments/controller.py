from modules.role_attachments.service import RoleAttachmentsService
from modules.role_attachments.mapper import RoleAttachmentsMapper

from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.users.service import UsersService

from werkzeug.exceptions import BadRequest, Forbidden, HTTPException
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
            username = userInformation['Username']

            requestBody = request.json
            paramsToCheck = ['profileId', 'roleId']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")

            userDTO = UsersService.getByUsername(username)
            if userDTO['profile'] and userDTO['profile']['id'] != requestBody['profileId']:
                raise Forbidden("Forbidden")
            
            roleAttachmentDTO = RoleAttachmentsService.create(requestBody['profileId'], requestBody['roleId'])
            return roleAttachmentDTO, 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/<roleAttachmentId>")
class RoleAttachmentsController(Resource):
    def delete(self, roleAttachmentId):
        try:
            userInformation = AuthService.validate(request.headers)
            username = userInformation['Username']

            userDTO = UsersService.getByUsername(username)

            RoleAttachmentsService.delete(roleAttachmentId, userDTO['profile']['id'])
            return { 'id': roleAttachmentId }, 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500