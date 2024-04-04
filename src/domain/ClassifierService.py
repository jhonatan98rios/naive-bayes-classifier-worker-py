import io
import json
import pickle
import pandas as pd
from src.domain.Classifier import Classifier
from src.domain.EventPayload import EventPayload
from src.infra.MongoDBRepository import MongoDBRepository
from src.infra.NaiveBayesClassifierGateway import NaiveBayesClassifier
from src.infra.S3Provider import S3Provider
from src.infra.SQSProvider import SQSProvider

class ClassifierService:
    def __init__(
            self, 
            sqs_provider: SQSProvider, 
            s3_provider: S3Provider, 
            mongodb_repository: MongoDBRepository, 
            naive_bayes_classifier: NaiveBayesClassifier
        ):
        self.sqs_provider = sqs_provider
        self.s3_provider = s3_provider
        self.mongodb_repository = mongodb_repository
        self.naive_bayes_classifier = naive_bayes_classifier


    def execute(self, body):

        event = self.get_event_payload_from_body(body)
        filename = f"model/{event.id}.model.pkl"

        try:
            csv = self.s3_provider.get_object(event.path)
            df = self.get_df_from_csv(csv)
            buffer, accuracy = self.train_model(df)
            self.s3_provider.send_object(filename, buffer)
            
            updated_classifier = {
                "id": event.id,
                "name": event.name,
                "description": event.description,
                "type": event.type,
                "path": filename,
                "accuracy": accuracy,
                "format": event.format,
                "isPublic": event.isPublic,
                "owners": event.owners,
                "rating": 0,
                "size": len(buffer.getbuffer()),
                "status": "ready"
            }

            self.mongodb_repository.update(event.id, updated_classifier)

        except Exception as err:

            updated_classifier = {
                "id": event.id,
                "name": event.name,
                "description": event.description,
                "type": event.type,
                "path": filename,
                "format": event.format,
                "isPublic": event.isPublic,
                "owners": event.owners,
                "status": "failed",
                "accuracy": 0,
                "rating": 0,
                "size": 0,
            }

            self.mongodb_repository.update(event.id, updated_classifier)
            raise Exception(f"Erro ao realizar o treinamento: {err}")
                
    
    def get_event_payload_from_body(self, body):
        try:
            payload = json.loads(body)
            event = EventPayload(
                id=payload["id"],
                name=payload["name"],
                description=payload["description"],
                type=payload["type"],
                path=payload["path"],
                format=payload["format"],
                isPublic=payload["isPublic"],
                owners=payload["owners"],
                status=payload["status"]
            )

            return event
        except Exception as err:
            raise Exception(f"Erro ao ler os dados: {err}")


    def get_df_from_csv(self, csv):
        try:
            buffer = io.BytesIO(csv)
            return pd.read_csv(buffer, delimiter=";")
        except Exception as err:
            raise Exception(f"Erro ao converter o csv em dataframe: {err}")
        
        
    def train_model(self, df):
        try:
            model, accuracy = self.naive_bayes_classifier.train(df)

            # Salvar o modelo treinado serializado em um buffer
            buffer = io.BytesIO()
            pickle.dump(model, buffer)
            buffer.seek(0)
                        
            return buffer, accuracy
        except Exception as err:
            raise Exception(f"Erro ao treinar o modelo: {err}")