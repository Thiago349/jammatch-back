from .service import UsersService
from .mapper import UsersMapper
from modules.auth.service import AuthService
from modules.profiles.service import ProfilesService
from modules.profiles.mapper import ProfilesMapper
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
                if (param in requestBody.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: '{', '.join(missingParams)}' required"}, 400
                
            userDTO = UsersService.create(requestBody['name'], requestBody['username'], requestBody['password'], requestBody['email'])
            return userDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
        

@api.route("/self")
class UserController(Resource):
    def get(self):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401
            username = userInformation['Username']

            userDTO = UsersService.getByUsername(username)
            if userDTO == None:
                return f"Not Found: No user with '{username}' username", 404
            return userDTO, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500