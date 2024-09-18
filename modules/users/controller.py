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
                
            userEntity, profileEntity = UsersService.create(requestBody['name'], requestBody['username'], requestBody['password'], requestBody['email'])
            userDTO = UsersMapper.entityToDTO(userEntity)
            profileDTO = ProfilesMapper.entityToDTO(profileEntity)
            userDTO['profile'] = profileDTO
            return userDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/<userId>")
class UserController(Resource):
    def get(self, userId):
        try:
            userInformation = AuthService.validate(request.headers)
            if userInformation == None: 
                return {"message": f"Unauthorized"}, 401

            userEntity, profileEntity = UsersService.getById(userId)
            if userEntity == None:
                return f"No user with '{userId}' id", 404

            userDTO = UsersMapper.entityToDTO(userEntity)
            
            if profileEntity != None:
                userDTO['profile'] = ProfilesMapper.entityToDTO(profileEntity)

            return userDTO, 200
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

            userEntity, profileEntity = UsersService.getByUsername(username)
            if userEntity == None:
                return f"No user with {username} username", 404

            userDTO = UsersMapper.entityToDTO(userEntity)

            if profileEntity != None:
                userDTO['profileId'] = ProfilesMapper.entityToDTO(profileEntity)['id']

            return userDTO, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500