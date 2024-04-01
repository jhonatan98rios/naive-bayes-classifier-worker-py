from src.infra.NaiveBayesClassifierGateway import NaiveBayesClassifier
from src.domain.ClassifierService import ClassifierService
from src.infra.MongoDBRepository import MongoDBRepository
from src.infra.S3Provider import S3Provider
from src.infra.SQSProvider import SQSProvider


class ClassifierController:
    
    @staticmethod
    def handle_message(message):
        body = message['Body']  # Supondo que o corpo da mensagem contenha o caminho do arquivo no S3

        sqs_provier = SQSProvider()
        s3_provider = S3Provider()
        mongodb_repository = MongoDBRepository()
        naive_bayes_classifier = NaiveBayesClassifier()

        classifier_service = ClassifierService(
            mongodb_repository=mongodb_repository,
            s3_provider=s3_provider,
            sqs_provider=sqs_provier,
            naive_bayes_classifier=naive_bayes_classifier
        )

        return classifier_service.execute(body)


