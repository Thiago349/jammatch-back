import boto3
import os

ADMIN_ACCESS_KEY_ID = os.environ['ADMIN_ACCESS_KEY_ID']
ADMIN_SECRET_ACCESS_KEY = os.environ['ADMIN_SECRET_ACCESS_KEY']


session = boto3.Session(
    aws_access_key_id = ADMIN_ACCESS_KEY_ID,
    aws_secret_access_key = ADMIN_SECRET_ACCESS_KEY,
    region_name='us-east-1'
)