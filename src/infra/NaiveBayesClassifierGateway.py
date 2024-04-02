import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

class NaiveBayesClassifier:
    def __init__(self):
        pass

    def train(self, df: pd.DataFrame):
        try:
            # Separar os dados de entrada (X) e os rótulos (y)
            X = df.drop('label', axis=1)
            y = df['label']

            # Dividir os dados em conjuntos de treinamento e teste
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Criar e treinar o modelo Gaussian Naive Bayes
            model = GaussianNB()
            model.fit(X_train, y_train)
            accuracy = self.calculate_accuracy(model, X_test, y_test)

            return model, accuracy
        except Exception as err:
            raise Exception(f"Erro ao treinar o modelo: {err}")
        
    
    def calculate_accuracy(self, model, X_test, y_test):
        try:
            # Fazer previsões nos dados de teste
            y_pred = model.predict(X_test)

            # Calcular a acurácia
            accuracy = accuracy_score(y_test, y_pred)
            return accuracy
        except Exception as err:
            raise Exception(f"Erro ao calcular a acurácia: {err}")