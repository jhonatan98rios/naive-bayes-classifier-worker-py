import boto3
from botocore.exceptions import ClientError

class SQSProvider:
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

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

    def receive_message(self, max_number_of_messages=1):
        try:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=max_number_of_messages
            )
            return response.get('Messages', [])
        except ClientError as e:
            print("Erro ao receber mensagens:", e)
            return []

    def delete_message(self, receipt_handle):
        try:
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Mensagem excluída.")
        except ClientError as e:
            print("Erro ao excluir mensagem:", e)