from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv.main import load_dotenv
import os

load_dotenv()

DATABASE_USER=os.environ['DATABASE_USER']
DATABASE_PASS=os.environ['DATABASE_PASS']
DATABASE_HOST=os.environ['DATABASE_HOST']
DATABASE_NAME=os.environ['DATABASE_NAME']

class MongoDBRepository:
    def __init__(self):
        self.connection()
        self.create_indexes()

        
    def connection(self):
        try:
            uri = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/?retryWrites=true&w=majority&appName=ClusterBlog"
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client["naive-bayes-classifier-database"]
            self.collection = self.db["classifiers"]

        except Exception as err:
            raise Exception(f"Connection Error: {err}")
        
    def create_indexes(self):
        try:
            # Verificando se o índice 'id' já existe
            if "id" not in self.collection.index_information():
                # Criando índice para o campo 'id' com um nome exclusivo
                self.collection.create_index("id", name="_id")
        except Exception as e:
            raise Exception(f"Erro ao criar índice: {e}")


    def readOneById(self, document_id: str):
        try:
            document = self.collection.find_one({"id": document_id})
            return document
        except Exception as err:
            raise Exception(f"Erro ao ler documento por ID: {document_id} \n {err}")

    def update(self, id, updated_object):
        try:
            result = self.collection.update_one({'id': id}, {'$set': updated_object})
            if result.modified_count == 0:
                raise ValueError("Documento não encontrado ou não atualizado.")
            else:
                print("Documento atualizado com sucesso.")
        except Exception as e:
            print("Erro ao atualizar documento:", e)