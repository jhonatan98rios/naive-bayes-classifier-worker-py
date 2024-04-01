import io
import boto3
import os
from dotenv.main import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION=os.environ['AWS_REGION']
BUCKET_NAME=os.environ['BUCKET_NAME']

class S3Provider:
    def __init__(self):
        self.bucket_name=BUCKET_NAME
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

    def getObject(self, object_key: str):
        try:
            # Recuperando o objeto do S3
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=object_key
            )
            # Lendo o conteúdo do objeto
            return response['Body'].read()
        
        except Exception as err:
            raise Exception(f"Erro ao recuperar objeto do S3: {err}")

