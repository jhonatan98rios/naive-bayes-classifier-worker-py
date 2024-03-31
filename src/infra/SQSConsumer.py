import boto3
import time

class SQSConsumer:
    def __init__(self, queue_url):
        self.sqs = boto3.client('sqs')
        self.queue_url = queue_url

    def process_message(self, message, function):
        print("Mensagem recebida:", message['Body'])

        # Aqui você pode adicionar lógica para processar a mensagem recebida

    def poll_messages(self, handler: function):
        while True:
            try:
                response = self.sqs.receive_message(
                    QueueUrl=self.queue_url,
                    MaxNumberOfMessages=1,
                    WaitTimeSeconds=20  # Tempo de espera máximo (até 20 segundos)
                )
                messages = response.get('Messages', [])
                for message in messages:
                    self.process_message(message, handler)
                    # Exclui a mensagem após processá-la
                    self.sqs.delete_message(
                        QueueUrl=self.queue_url,
                        ReceiptHandle=message['ReceiptHandle']
                    )
            except Exception as e:
                print("Erro ao receber mensagens:", e)
            time.sleep(1)  # Espera 1 segundo antes de consultar a fila novamente

