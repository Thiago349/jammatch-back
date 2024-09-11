from services.cognito.client import CognitoClient


def authenticate(username: str, password: str):
    try:
        return CognitoClient.initiateAuth(username, password)
    except Exception as e:
        print("ERROR: ", e)
        return None
    

def validate(token: str):
    try:
        return CognitoClient.getUser(token)
    except Exception as e:
        print("ERROR: ", e)
        return None