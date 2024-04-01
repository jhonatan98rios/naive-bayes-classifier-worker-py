import os
import boto3
from botocore.exceptions import ClientError
from dotenv.main import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION=os.environ['AWS_REGION']
QUEUE_URL=os.environ['QUEUE_URL']

class SQSProvider:
    def __init__(self):
        self.queue_url = QUEUE_URL
        self.sqs = boto3.client(
            'sqs',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

    def send_message(self, message_body):
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body
            )
            return response
        except ClientError as e:
            print("Erro ao enviar mensagem:", e)
            return None


    def delete_message(self, receipt_handle):
        try:
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Mensagem excluída.")
        except ClientError as e:
            print("Erro ao excluir mensagem:", e)
