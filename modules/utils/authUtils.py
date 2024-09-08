import os
import hmac
import hashlib
import base64


def getSecretHase(username, clientId, clientSecret):
        msg = username + clientId
        dig = hmac.new(str(clientSecret).encode('utf-8'),
                        msg=str(msg).encode('utf-8'),
                        digestmod=hashlib.sha256).digest()
        return base64.b64encode(dig).decode()


def verifyToken(authorization):
        autorizationString = str(authorization)
        if 'Bearer ' != autorizationString[:7]:
                return None
        return autorizationString[7:]