from modules.auth.repository import AuthRepository
from modules.utils.authUtils import verifyToken


class AuthService:  
    def authenticate(username, password):
        auth = AuthRepository.authenticate(username, password)
        return auth
    

    def validate(headers):
        if ('Authorization' in headers) == False:
            return None
        
        token = verifyToken(headers['Authorization'])
        if token == None:
            return None
        
        userInformation = AuthRepository.validate(token)
        return userInformation