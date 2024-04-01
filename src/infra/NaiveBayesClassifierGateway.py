import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

class NaiveBayesClassifier:
    def __init__(self):
        pass

    def train(self, df: pd.DataFrame):
        
        # Separar os dados de entrada (X) e os rótulos (y)
        X = df.drop('label', axis=1)
        y = df['label']

        # Dividir os dados em conjuntos de treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Criar e treinar o modelo Gaussian Naive Bayes
        model = GaussianNB()
        model.fit(X_train, y_train)

        return model