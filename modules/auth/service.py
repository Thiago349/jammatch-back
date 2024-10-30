from modules.auth.repository import AuthRepository
from modules.utils.authUtils import verifyToken
from werkzeug.exceptions import Unauthorized


class AuthService:  
    def authenticate(username, password):
        auth = AuthRepository.authenticate(username, password)
        return auth
    

    def refresh(username, refreshToken):
        auth = AuthRepository.refresh(username, refreshToken)
        return auth
    

    def validate(headers):
        if 'Authorization' not in headers:
            raise Unauthorized("Unauthorized")
        
        token = verifyToken(headers['Authorization'])
        if token == None:
            raise Unauthorized("Unauthorized")
        
        userInformation = AuthRepository.validate(token)
        return userInformation