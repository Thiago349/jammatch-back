import modules.auth.repository as repository
from modules.utils.authUtils import verifyToken


class AuthService:  
    def authenticate(username, password):
        auth = repository.authenticate(username, password)
        return auth
    

    def validate(headers):
        if ('Authorization' in headers) == False:
            return None
        
        token = verifyToken(headers['Authorization'])
        if token == None:
            return None
        
        userInformation = repository.validate(token)
        return userInformation