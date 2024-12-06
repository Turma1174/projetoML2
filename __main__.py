import os
import subprocess
import asyncio
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def execute_notebook(notebook_path, output_path=None):
    """
    Executa um notebook Jupyter (.ipynb) usando nbconvert.
    
    Args:
        notebook_path (str): Caminho para o notebook a ser executado.
        output_path (str): Caminho para salvar o notebook executado (opcional).
    """
    try:
        output_option = ["--output", output_path] if output_path else []
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute"] + output_option + [notebook_path],
            check=True
        )
        print(f"✔️ Concluído: {notebook_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar: {notebook_path}\n{e}")

def main():
    # Diretório base
    notebooks_dir = "./"

    # Lista de notebooks
    """
    notebooks = [
        "exploratoria.ipynb",
        "cleaned_data.ipynb",    
        "regressao_svr.ipynb",
        "regressao_bagging_boosting.ipynb",
        "regressao_mlp.ipynb",
        "classificador_mlp.ipynb",
        "clusterizacao_kmeans.ipynb",
        "clusterizacao_dbscan.ipynb"    
    ]
    """
    notebooks = [
        "exploratoria.ipynb",
        "cleaned_data.ipynb",    
        "regressao_svr.ipynb",
        "regressao_bagging_boosting.ipynb",
        "regressao_mlp.ipynb",
        "classificador_mlp.ipynb",
        "clusterizacao_kmeans.ipynb",
        "clusterizacao_dbscan.ipynb"    
    ]


    # Executa todos os notebooks
    for notebook in notebooks:
        notebook_path = os.path.join(notebooks_dir, notebook)
        print(f"▶️ Executando: {notebook}")
        execute_notebook(notebook_path)

if __name__ == "__main__":
    main()