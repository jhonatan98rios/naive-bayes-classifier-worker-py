import io
import boto3
import os

class S3Provider:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('AWS_REGION')
        )
        self.bucket_name = os.environ.get('BUCKET_NAME')

    def getObject(self, object_key: str):
        try:
            # Recuperando o objeto do S3
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=object_key
            )
            # Lendo o conteúdo do objeto
            object_content = response['Body'].read()
            return  io.BytesIO(object_content)
        
        except Exception as err:
            raise Exception(f"Erro ao recuperar objeto do S3: {err}")

