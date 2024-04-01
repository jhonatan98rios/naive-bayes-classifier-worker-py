import io
import json
import joblib
import pandas as pd
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
        id, path = self.get_data_from_body(body)
        csv = self.s3_provider.getObject(path)
        df = self.get_df_from_csv(csv)

        model = self.naive_bayes_classifier.train(df)
        model_name = f"{id}.model.pkl"
        # Salvar o modelo treinado em um arquivo
        joblib.dump(model, model_name)

        
    
    def get_data_from_body(self, body):
        try:
            payload = json.loads(body)
            return payload["id"], payload["path"]
        except Exception as err:
            raise Exception(f"Erro ao ler os dados: {err}")


    def get_df_from_csv(self, csv):
        try:
            buffer = io.StringIO(csv.decode('utf-8'))
            return pd.read_csv(buffer, error_bad_lines="skip")
        except Exception as err:
            raise Exception(f"Erro ao converter o csv em dataframe: {err}")