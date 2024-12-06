from src import eda, analysis, correlations, plots, ml_model

# Caminhos para os datasets
data_path = "data/diamons.csv"
cleaned_path = "data/cleaned.csv"
train_path = "data/train.csv"
test_path = "data/test.csv"

def main():
    # Etapa 1: Tratamento de dados
    eda.clean_data(data_path, cleaned_path)
    
    # Etapa 2: Análise descritiva
    analysis.describe_data(cleaned_path)
    
    # Etapa 3: Correlações
    correlations.calculate_correlations(cleaned_path)
    
    # Etapa 4: Visualizações
    plots.generate_plots(cleaned_path)
    
    # Etapa 5: Modelagem preditiva
    ml_model.train_model(train_path, test_path)

if __name__ == "__main__":
    main()