# Funções para cálculos de correlação

import pandas as pd

def calculate_correlations(input_path):
    """
    Calcula e exibe a matriz de correlação.
    """
    df = pd.read_csv(input_path)
    
    # Matriz de correlação
    correlations = df.corr()
    print(correlations)
