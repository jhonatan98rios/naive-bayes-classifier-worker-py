from src.infra.ClassifierService import ClassifierService
from src.infra.MongoDBRepository import MongoDBRepository
from src.infra.S3Provider import S3Provider
from src.infra.SQSProvider import SQSProvider


class ClassifierController:
    
    @staticmethod
    def handle_message(self, message):
        body = message['Body']  # Supondo que o corpo da mensagem contenha o caminho do arquivo no S3
        path = body['path']

        sqs_provier = SQSProvider()
        s3_provider = S3Provider()
        mongodb_repository = MongoDBRepository()

        classifier_service = ClassifierService(
            mongodb_repository=mongodb_repository,
            s3_provider=s3_provider,
            sqs_provider=sqs_provier
        )

        classifier_service.execute(message)


