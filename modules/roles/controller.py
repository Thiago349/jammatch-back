from modules.roles.service import RolesService

from modules.auth.service import AuthService

from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Roles", path="/api/v1/roles"
)


@api.route("")
class RolesController(Resource):
    def get(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                raise Exception("Unauthorized", 401)

            requestArgs = request.args
            if 'profileType' not in requestArgs.keys():
                raise Exception("Bad Request: 'profileType' required", 400)
            
            roleDTOs = RolesService.getByProfileType(requestArgs['profileType'])
            return roleDTOs, 200
        except Exception as e:
            if isinstance(e, Exception):
                return {"message": e.args[0]}, e.args[1]
            
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
