from .service import RolesService
from .mapper import RolesMapper

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
                return {"message": f"Unauthorized"}, 401

            requestArgs = request.args
            paramsToCheck = ['profileType']
            missingParams = []
            for param in paramsToCheck:
                if (param in requestArgs.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: '{', '.join(missingParams)}' required"}, 400

            roleEntities = RolesService.getByProfileType(requestArgs['profileType'])
            roleDTOs = []
            for roleEntity in roleEntities:
                roleDTOs.append(RolesMapper.entityToDTO(roleEntity))
            return roleDTOs, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
