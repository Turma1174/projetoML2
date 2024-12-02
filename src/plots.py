# Funções para criação de gráficos

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_plots(input_path):
    """
    Gera gráficos para o dataset.
    """
    df = pd.read_csv(input_path)
    
    # Exemplo: Histograma para uma feature
    sns.histplot(df['carat'], kde=True)
    plt.title("Distribuição de Carat")
    plt.show()
