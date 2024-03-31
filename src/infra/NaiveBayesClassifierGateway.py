import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib

# Carregar os dados do arquivo CSV
df = pd.read_csv('dados_acao.csv')


df.head(1).to_json('./teste.json', 'records')



labels = [
    'await',
    'sell',
    'buy'
]

class NaiveBayesClassifier:
    def __init__(self):
        pass

    def train(self, model_id: str, df: pd.DataFrame):
        
        # Separar os dados de entrada (X) e os rótulos (y)
        X = df.drop('label', axis=1)
        y = df['label']

        # Dividir os dados em conjuntos de treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Criar e treinar o modelo Gaussian Naive Bayes
        model = GaussianNB()
        model.fit(X_train, y_train)

        model_name = f"{model_id}.model.pkl"

        # Salvar o modelo treinado em um arquivo
        joblib.dump(model, model_name)