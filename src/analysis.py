# Funções para análise descritiva

import pandas as pd

def describe_data(input_path):
    """
    Exibe informações descritivas do dataset.
    """
    df = pd.read_csv(input_path)
    
    # Resumo estatístico
    print(df.describe())
    
    # Informações do dataset
    print(df.info())
