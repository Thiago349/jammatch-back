from modules.roles.service import RolesService
from modules.auth.service import AuthService

from werkzeug.exceptions import BadRequest, Unauthorized, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Roles", path="/api/v1/roles"
)


@api.route("")
class RolesController(Resource):
    def get(self):
        try:
            AuthService.validate(request.headers)

            requestArgs = request.args
            if 'profileType' not in requestArgs.keys():
                raise BadRequest("Bad Request: 'profileType' required")
            
            roleDTOs = RolesService.getByProfileType(requestArgs['profileType'])
            return roleDTOs, 200
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
