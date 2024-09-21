import os
from modules.utils.authUtils import getSecretHase
from ..session import session

client = session.client('cognito-idp')
COGNITO_CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
COGNITO_CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']


class CognitoClient:
    def signUp(username, password, email):
        client.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            SecretHash=getSecretHase(username, COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET),
            Username=username,
            Password=password,
            UserAttributes=[{
                "Name": "email",
                "Value": email
            }]
        )
    
    
    def initiateAuth(username, password):
        response = client.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH': getSecretHase(username, COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET)
            },
        )
        
        return response
    

    def refreshAuth(username, token):
        response = client.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': token,
                'SECRET_HASH': getSecretHase(username, COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET)
            },
        )
        
        return response
    

    def getUser(token):
        response = client.get_user(
            AccessToken=token
        )

        return response