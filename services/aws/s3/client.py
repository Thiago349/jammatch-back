import os
import werkzeug.datastructures
from ..session import session

client = session.client('s3')
S3_BUCKET_ID = os.environ['S3_BUCKET_ID']
S3_BUCKET_SECRET = os.environ['S3_BUCKET_SECRET']


class BucketClient:
    def uploadFile(file: werkzeug.datastructures.FileStorage, bucketName: str, objectName: str):
        client.upload_fileobj(
            file,
            bucketName,
            objectName,
            ExtraArgs = { 'ContentType': file.content_type }
        )