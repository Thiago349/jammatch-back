from .service import UsersService
from .mapper import UsersMapper
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Users", path="/api/v1/users"
)


@api.route("/")
class UsersController(Resource):
    def get(self):
        try:
            requestArgs = request.args
            page = 1
            limit = 10
            if 'limit' in requestArgs.keys():
                limit = int(requestArgs['limit'])
            if 'page' in requestArgs.keys():
                page = int(requestArgs['page'])
            
            userEntities = UsersService.getUsers(limit, page)['data']
            userDTOs = []
            for userEntity in userEntities:
                userDTOs.append(UsersMapper.userEntityToDTO(userEntity))
            return userDTOs, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
        
    
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['name', 'description', 'username', 'email']
            missingParams = []
            for param in paramsToCheck:
                if (param in requestBody.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: {', '.join(missingParams)}"}, 400
            
            userEntity = UsersService.createUser(requestBody['name'], requestBody['description'], requestBody['username'], requestBody['email'])['data']
            userDTO = UsersMapper.userEntityToDTO(userEntity)
            return userDTO, 201
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/<userId>")
class UserController(Resource):
    def get(self, userId):
        try:
            userEntity = UsersService.getUserById(userId)['data']
            if userEntity == None:
                return f"Bad Request: No request with {userId} id", 400

            userDTO = UsersMapper.userEntityToDTO(userEntity)
            return userDTO, 200
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500