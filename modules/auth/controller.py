from modules.auth.service import AuthService

from werkzeug.exceptions import BadRequest, Unauthorized, HTTPException
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
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: {', '.join(missingParams)}")
            
            authDTO = AuthService.authenticate(requestBody['username'], requestBody['password'])
            
            if authDTO:
                return {
                    "token": authDTO['AuthenticationResult']['AccessToken'], 
                    "refreshToken": authDTO['AuthenticationResult']['RefreshToken']
                }, 201
            else:
                raise Unauthorized("Unauthorized")

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500


@api.route("/refresh")
class AuthController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['username', 'refreshToken']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: {', '.join(missingParams)}")
                            
            authDTO = AuthService.refresh(requestBody['username'], requestBody['refreshToken'])

            if authDTO:
                return {
                    "token": authDTO['AuthenticationResult']['AccessToken']
                }, 201
            else:
                raise Unauthorized("Unauthorized")
            
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
