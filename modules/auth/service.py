import modules.auth.repository as repository


class AuthService:  
    def authenticate(username, password):
        auth = repository.authenticate(username, password)
        return auth
    

    def validate(token):
        user = repository.validate(token)
        return user