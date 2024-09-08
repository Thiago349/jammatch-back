import boto3 
import os
from ..utils.authUtils import getSecretHase

cognitoClient = boto3.client('cognito-idp', region_name='us-east-1')
COGNITO_CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
COGNITO_CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']


def authenticate(username: str, password: str):
    try:
        response = cognitoClient.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH': getSecretHase(username, COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET)
            },
        )
        
        return response
    except Exception as e:
        print(e)
        return None
    

def validate(token: str):
    try:
        response = cognitoClient.get_user(
            AccessToken=token
        )
        return response
    except Exception as e:
        return None