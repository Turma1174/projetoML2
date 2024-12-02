# Funções para tratamento de dados

import pandas as pd

def clean_data(input_path, output_path):
    """
    Limpa o dataset e salva no arquivo especificado.
    """
    df = pd.read_csv(input_path)
    
    # Exemplo de limpeza: remoção de duplicatas e valores nulos
    df = df.drop_duplicates().dropna()
    
    # Salvar o dataset tratado
    df.to_csv(output_path, index=False)
    print(f"Dataset tratado salvo em: {output_path}")
