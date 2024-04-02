import boto3
import time
import os
from dotenv.main import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION=os.environ['AWS_REGION']
QUEUE_URL=os.environ['QUEUE_URL']

class SQSConsumer:
    def __init__(self):

        print(QUEUE_URL)
        self.queue_url=QUEUE_URL
        self.sqs = boto3.client(
            'sqs',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

    def poll_messages(self, handler):
        print('Starting...')
        while True:
            print('Listening...')
            try:
                response = self.sqs.receive_message(
                    QueueUrl=self.queue_url,
                    MaxNumberOfMessages=1,
                    WaitTimeSeconds=20
                )
                messages = response.get('Messages', [])
                for message in messages:
                    handler(message)

                    # Exclui a mensagem após processá-la
                    # self.sqs.delete_message(
                    #     QueueUrl=self.queue_url,
                    #     ReceiptHandle=message['ReceiptHandle']
                    # )
            except Exception as e:
                print("Erro ao processar o evento:", e)
            

