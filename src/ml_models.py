# Funções para modelagem de Machine Learning

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(train_path, test_path):
    """
    Treina um modelo de Machine Learning e exibe os resultados.
    """
    # Carregar datasets
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    
    # Separar features e target
    X_train = train.drop(columns=['price'])
    y_train = train['price']
    X_test = test.drop(columns=['price'])
    y_test = test['price']
    
    # Treinamento do modelo
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Avaliação
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
