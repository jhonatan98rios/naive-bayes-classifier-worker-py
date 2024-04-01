from src.infra.ClassifierController import ClassifierController
from src.infra.SQSConsumer import SQSConsumer

sqs_consumer = SQSConsumer()

sqs_consumer.poll_messages(
   handler=ClassifierController.handle_message
)




