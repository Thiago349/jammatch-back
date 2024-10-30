from modules.users.service import UsersService
from modules.users.mapper import UsersMapper
from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.profiles.mapper import ProfilesMapper

from werkzeug.exceptions import BadRequest, NotFound, Forbidden, Unauthorized, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Users", path="/api/v1/users"
)


@api.route("")
class UsersController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['name', 'username', 'password', 'email']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")
                
            userDTO = UsersService.create(requestBody['name'], requestBody['username'], requestBody['password'], requestBody['email'])
            return userDTO, 201
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
        

@api.route("/self")
class UserController(Resource):
    def get(self):
        try:
            userInformation = AuthService.validate(request.headers)
            username = userInformation['Username']

            userDTO = UsersService.getByUsername(username)
            return userDTO, 200
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500