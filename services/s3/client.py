import boto3 
import os

client = boto3.client('s3', region_name='us-east-1')
S3_CLIENT_ID = os.environ['S3_CLIENT_ID']
S3_CLIENT_SECRET = os.environ['S3_CLIENT_SECRET']

