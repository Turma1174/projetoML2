![Logo da Ada Tech Crusos](./assets/LogoAdaCabecalho.png)

<hr>

<H2 align="center">
  PROJETO MACHINE LEARNING | SANTANDER CODERS 2024 | ADA TECH
  
  Dataset Diamantes (Kaggle)
</H2>


<p align="center">
   <img src="https://img.shields.io/static/v1?label=STATUS&message=%20EM CONSTRUÇÃO&color=RED&style=for-the-badge" #vitrinedev/>
</p>


## Tópicos 

- [Regras de Colaboração](#regras-de-colaboração)

- [Descrição do projeto](#descrição-do-projeto)

- [Regras](#regras)

- [Funcionalidades](#funcionalidades)

- [Desafios](#desafios)

- [Ferramentas utilizadas](#ferramentas-utilizadas)

- [Estrutura do Projeto](#estrutura-do-projeto)

- [Acesso ao projeto](#acesso-ao-projeto)

- [Executando o projeto](#executando)

- [Colaboradores](#colaboradores)

## Regras de Colaboração

Após confirmação do convite no GitHub, recomenda-se:

1. Crie um repositorio local;
2. Clone o projeto: 
```bash
git clone "https://github.com/Turma1174/projetoML2"
```
3. Crie uma branch com seu nome:
```bash
git checkout -b 'seu_nome' 
```
4. Agora você irá trabalhar dentro da sua branch (verifique no VS Code se está na sua branch)
5. Para subir sua contribuição para a "main", siga os passos:
```bash
git add .
git commit -m "sua contribuição"
git push origin "seu_nome"
```
6. Atualize a "main": 
```bash
git checkout main
git merge "seu_nome"
```
7. Após "mergear", informe ao grupo que você atualizou a "main";
8. Então, os demais colabs devem atualizar a sua "main":
```bash
git pull origin main
```

## Descrição do projeto

Este projeto realiza análises exploratórias, tratamento de dados e modelagem preditiva usando dados de diamantes.

`Origem: ` O dataset diamonds está disponível no Kaggle e faz parte do pacote ggplot2 em R. Ele foi construído para exemplificar análises de regressão, visualização de dados e modelagem estatística.

`Motivação: ` A ideia é ajudar estudantes e profissionais a explorar dados reais sobre diamantes, analisando como características (como quilates, corte e cor) influenciam o preço de mercado.

Para atingir os objetivos do projeto, a entrega deve contemplar as três etapas:

`Descrição 1` Na etapa de análise exploratória de dados, o grupo seja capaz de entender o problema de negócio ao qual o dataset escolhido se insere, sabendo levantar perguntas de interesse, que deverão ser respondidas com embasamentos nas análises de dados (avaliações gráficas, estatísticas e afins);

`Descrição 2` Para a avaliação de segmentação, espera-se que o grupo seja capaz de encontrar agrupamentos no conjunto de dados, em relação a variáveis de interesse para o problema proposto. Por exemplo, pensando em um dataset de compras de determinados produtos, é possível associar perfis de consumidores a padrões específicos de gastos? Como isso pode ser feito?;

`Descrição 3` Por fim, a análise preditiva pressupõe a utilização de modelos, a escolha do grupo, para predizer a(s) variável(eis) de interesse dos problemas levantados pelo grupo. Apesar de ser interessante vocês praticarem os algoritmos estudados neste módulo, comparações com modelos previamente estudados (Machine Learning I e II).

## Regras
Com o ferramental em análise e em ciência de dados adquirido até o momento, a ideia é que, com este projeto, vocês possam avaliar um dataset sob três óptica (regras):

`Regra 1:` Uma análise exploratória de dados;

`Regra 2:` Uma análise de segmentação;

`Regra 3:` Uma análise preditiva.

## Funcionalidades

`Funcionalidades:` Modelagem preditiva de Classificação/Regressão com Machine Learning.

## Desafios

`Desafios:` Em virtude dos requisitos `Regras (2) e (3)` mencionados, a base de dados deve possuir uma variável que deverá ser predita pelos modelos que vocês desenvolverão.

## Ferramentas utilizadas

[![My Skills](https://skillicons.dev/icons?i=git,github,python)](https://skillicons.dev)

## Estrututra do Projeto

```bash
project/
│
├── assets/                 # Imagens e documentos de referencia
├── data/                   # Diretório para os datasets
│   ├── diamonds.csv        # Dataset original
│   └── cleaned.csv         # Dataset tratado
│                           # Diretório para funções específicas
├── exploratoria.ipynb      # Análises descritivas
├── cleaned_data.ipynb      # Tratamento de dados
├── regressao_svr.ipynb     # Modelagem de Regressão com SVM
├── regressao_bagging.ipynb # Modelagem de Regressão com Ensemble
├── regressao_mlp.ipynb     # Modelagem de Regressão com MLP
├── classificacao_mlp.ipynb # Modelagem de Classificação com MLP
├── clusterizacao_kmeans    # Modelagem de Clusterização com KMEANS
└── clusterizacao_dbscan    # Modelagem de Clusterização com DBSCAN
│
├── __main__.py             # Ponto de entrada do programa
│
├── requirements.txt        # Dependências do projeto
│
└── README.md               # Documentação do projeto
│
└── RESULTADOS.md           # Resultados do projeto

```

## Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/Turma1174/projetoML2/).

## Executando

1. Instale as dependências:
  - A execução pode demandar tempo e recursos do dispositivo local (consumo de memória ou travamento).
  - Para executar o pacote do Projeto Diamonds, execute via terminal/prompt:
  
  ```bash
   pip install -r requirements.txt
   python __main__.ipynb
  ```

## Colaboradores

| [<img src="https://avatars.githubusercontent.com/u/85369108?v=4" width=115> <br><sub>Instrutor ADA Romero Carvalho</sub>](https://github.com/RomeroFC1301) |  [<img src="https://avatars.githubusercontent.com/u/20822673?v=4" width=115><br><sub>André Filipe</sub>](https://github.com/filipester) | [<img src="https://avatars.githubusercontent.com/u/117116076?v=4" width=115> <br><sub>Gabriel Alencar</sub>](https://github.com/devalenca) | [<img src="https://avatars.githubusercontent.com/u/98609170?v=4" width=115><br><sub>Gabriel Makhoul</sub>](https://github.com/GMakhoul) | [<img src="https://avatars.githubusercontent.com/u/170963236?s=96&v=4" width=115><br><sub>João Oliveira</sub>](https://github.com/jjofilho) | 
| :---: | :---: | :---: | :---: | :---: |
