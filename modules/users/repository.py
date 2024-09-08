import boto3
import os
import uuid
from alchemy import db_session
from .entity import User
from ..utils.authUtils import getSecretHase

cognitoClient = boto3.client('cognito-idp', region_name='us-east-1')
COGNITO_CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
COGNITO_CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']


def getUsersPage(limit: int, page: int):
    try:
        users: User = db_session.query(User
            ).order_by(User.created_at.desc()
                ).limit(limit
                    ).offset(limit * (page - 1)
                        ).all()
        return users
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None
    

def getUserById(userId: uuid.uuid4):
    try:
        user: User = db_session.query(User
            ).filter(User.id == userId
                ).first()
        return user
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def getUserByUsername(username: str):
    try:
        user: User = db_session.query(User
            ).filter(User.username == username
                ).first()
        return user
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 
    

def createUser(name: str, description: str, username: str, password: str, email: str):
    try:
        userEntity = User(
            name = name,
            description = description,
            username = username,
            email = email
        )
        db_session.add(userEntity)
        db_session.flush()
        
        cognitoClient.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            SecretHash=getSecretHase(username, COGNITO_CLIENT_ID, COGNITO_CLIENT_SECRET),
            Username=username,
            Password=password,
            UserAttributes=[{
                "Name": "email",
                "Value": email
            }]
        )

        db_session.commit()

        return userEntity
    except Exception as e:
        print(f"ERROR: {e}")
        db_session.rollback()
        return None 