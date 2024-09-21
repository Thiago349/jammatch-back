from .service import AuthService
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Auth", path="/api/v1/auth"
)


@api.route("")
class AuthController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['username', 'password']
            missingParams = []
            for param in paramsToCheck:
                if (param in requestBody.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: {', '.join(missingParams)}"}, 400
            
            authDTO = AuthService.authenticate(requestBody['username'], requestBody['password'])
            
            if authDTO:
                return {
                    "token": authDTO['AuthenticationResult']['AccessToken'], 
                    "refreshToken": authDTO['AuthenticationResult']['RefreshToken']
                }, 201
            else:
                return {"message": "Unauthorized"}, 401
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500


@api.route("/refresh")
class AuthController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['username', 'refreshToken']
            missingParams = []
            for param in paramsToCheck:
                if (param in requestBody.keys()) == False:
                    missingParams.append(param)
            if len(missingParams) > 0:
                return {"message": f"Bad Request: {', '.join(missingParams)}"}, 400
                            
            authDTO = AuthService.refresh(requestBody['username'], requestBody['refreshToken'])

            if authDTO:
                return {
                    "token": authDTO['AuthenticationResult']['AccessToken']
                }, 201
            else:
                return {"message": "Unauthorized"}, 401
        except Exception as e:
            api.logger.error("Error: %s", str(e))
            return {"message": f"Internal Server Error: {str(e)}"}, 500
