# PRINCIPAIS RESULTADOS DO PROJETO DIAMONDS

## 1. Exploratória do Dataset

### **1.1 Origem e Motivação do Dataset**

- **Origem:** O _dataset diamonds_ está disponível no Kaggle e faz parte do pacote `ggplot2` em R. Ele foi construído para exemplificar análises de regressão, visualização de dados e modelagem estatística.

- **Motivação:** A ideia é ajudar estudantes e profissionais a explorar dados reais sobre diamantes, analisando como características (como quilates, corte e cor) influenciam o preço de mercado.

### **1.2 Representatividade no Mercado de Diamantes**

- **Cenário:** O _dataset_ contém mais de 53 mil registros e se baseia em métricas padrão do mercado (quilates, corte, cor, claridade e preço).

  ![Dataset Original](./assets/DatasetOriginal.png)

- **Limitações:** Ele pode não capturar toda a dinâmica do mercado real, como flutuações de preços baseadas em demanda, sazonalidade ou negociações específicas. Além disso, os dados podem ser simplificados e não consideram fatores como origem ética ou certificação de procedência, que afetam o valor.

- **Considerações:** Ele é um bom ponto de partida para modelagem, mas precisaria de complementos para representar o mercado atual de forma mais robusta.

### **1.3 Aspectos Importantes para Conferir no Dataset**

1. **Consistência dos dados:**

   - Verificar se todas as variáveis estão bem preenchidas e sem valores ausentes.
   - Identificar possíveis _outliers_, especialmente em preços e quilates.

   ![Outliers dataset original](./assets/Outliers1.png)

   ![Outliers após o preprocessamento](./assets/Outliers2.png)

2. **Correlação entre variáveis:**

   - Explorar a relação entre características físicas (como corte, cor, claridade) e o preço para confirmar se as tendências estão alinhadas com o mercado.

   ![Correlação](./assets/Correlacao.png)

3. **Distribuição dos dados:**

   - Conferir a distribuição das variáveis contínuas (como quilates e preço) e categóricas (como corte e cor) para garantir que são representativas.

   ![Distribuição](./assets/Distribuicao.png)

4. **Qualidade da categorização:**

   - Avaliar se as categorias de "cut", "color" e "clarity" estão claras e consistentes.

   ![Qualidade](./assets/CorPreco.png)

### **1.4 Novas Features a partir das Existentes**

- **Relação Preço x Quilates:** Criar uma feature com o preço por quilate para facilitar análises de custo-benefício.

  ![Quilates](./assets/Quilates.png)

- **Interação entre Variáveis:**

  - Combinar "cut", "color" e "clarity" em uma _feature_ composta, como um índice de qualidade geral.

  - Normalizar os preços para análise relativa dentro de categorias de corte.

- **Clusters de Preços:** Utilizar técnicas como _k-means_ para categorizar os diamantes em grupos de preços similares, facilitando análises segmentadas.

### **1.5 Pontos Relevantes**

1. **Modelagem Apropriada:**

   - O problema principal é prever o preço (variável contínua), então os modelos de regressão (linear, árvore de decisão, _random forest_, ou _gradient boosting_) seriam os mais indicados.

   ![Aprendizado](./assets/Aprendizado.png)

2. **Análise de Feature Importance:**

   - Utilizar técnicas como SHAP ou permutação de importância para verificar o impacto de cada variável no preço.

3. **Engenharia de Dados:**

   - Com o Dataset limpo, considerar transformar "cut", "color" e "clarity" em variáveis numéricas ou _embeddings_ categóricos para melhorar o desempenho de modelos baseados em aprendizado profundo.

   ![Dataset Limpo para Modelagem](./assets/DatasetLimpo.png)

4. **Validação e Testes:**

   - Dividir os dados com atenção (por exemplo, _stratified splitting_ para manter proporções entre categorias) e validar o modelo com métricas adequadas como RMSE ou MAE.

## **2. Regressões e Classificações Preditivas**

### **2.1 Modelagem para regressão com Ensemble e MLP**

1. **Bagging** - Método que combina múltiplos modelos independentes para maior robustez.

   ```
   Resultados:
   MSE: 294405.62
   R²: 0.98
   RMSE: 542.59
   ```

2. **Boosting** - Modelos sequenciais que corrigem erros do anterior, como Gradient Boosting e XGBoost.

   ```
   Resultados:
   MSE: 280468.76
   R²: 0.98
   RMSE: 529.59
   ```

3. **SVR** - Modelagem que maximiza margens e explora diferentes kernels.

   ```
   Resultados:
   MSE: 6938259.41
   R² Score: 0.56
   RMSE: 2634.06
   ```

4. **MLP Regressor** - Rede neural ajustada para capturar relações complexas.
   ```
   Resultados:
   MSE: 335075.82
   RMSE: 578.86
   R² Score: 0.98
   ```

### **2.2 Modelagem com Support Vector Regressor**

1. **SVR** 

   - Ajusta uma função (geralmente não linear) que prevê os valores da variável-alvo com base nas variáveis de entrada.

2. **Pré-processamento**

   - Padronização de variáveis numéricas: Ajuste para média 0 e desvio padrão 1.
   - Codificação de variáveis categóricas: OrdinalEncoder.

3. **Pipeline Integrado**

   - Combinação de pré-processamento e modelo para facilitar treinamento e predição.
   - Utilização do SVR com kernel RBF para capturar padrões não lineares nos dados.

4. **Avaliação do Modelo**

   ```
   RMSE (Erro Quadrático Médio Root): Representa o erro médio da predição.
   MSE (Erro Quadrático Médio): Média dos erros ao quadrado.
   R² Score: Percentual de variação explicada pelo modelo.
   ```

5. **Resultados obtidos**

   ```
   RMSE: 2634.06
   MSE:  6938259.41
   R² Score: 0.56
   ```

6. **Gráfico de dispersão: valores reais vs previstos**

   - Um bom modelo terá pontos próximos à linha diagonal vermelha, indicando que os valores previstos estão próximos aos reais.

   ![Gáfico de Dispersão](assets/dispersaoSVR.png)


### **2.3 Modelagem para Regressão com MPL**

1. **Rede Neural (MLP)**

   - A Rede Neural é como um cérebro de computador que aprende a partir de exemplos. Ela olha para as características dos diamantes e tenta descobrir qual é o padrão que faz o preço ser maior ou menor. Ela é muito boa em perceber coisas que são bem complicadas e difíceis de ver a olho nu.

2. **Pré-processamento**

   - Padronização de variáveis numéricas: StandardScaler.
   - Codificação de variáveis categóricas: OrdinalEncoder.

3. **Pipeline Integrado**

   - Combinação de pré-processamento e modelo em um pipeline.
   - Utilização do MLP Regressor, uma rede neural com as seguintes configurações:
   - Camadas ocultas: 2 camadas (100 neurônios na primeira, 50 na segunda).
   - Iterações máximas: 500 para garantir treinamento adequado.

4. **Resultados obtidos**

   ```
   RMSE: 578.86
   MSE: 335075.82
   R² Score: 0.98
   ```

5. **Gráfico de Erro Residual**

   - Este gráfico mostra a diferença entre os valores reais e os valores previstos. Quanto mais próximos de zero estiverem os erros, melhor.

   ![gráfico de Erro Residual](assets/ErroResidualMPL.png)

6. **Gráfico de Dispersão - Valores Reais vs Preditos**

   - Este gráfico ajuda a ver como os valores previstos se comparam aos valores reais. Quanto mais próximos da linha reta (linha de identidade) os pontos estiverem, melhor o modelo.

   ![Gráfico de Dispersão](assets/dispersaoMPL.png)


7. **Considerações sobre a aplicação do SVR e do MPL**

   - O modelo MLP provavelmente teve um desempenho melhor devido à sua capacidade de aprender padrões complexos e não lineares nas variáveis, o que é crucial para um problema desse, a previsão de preços de diamantes, onde várias interações não lineares podem estar em jogo. 

   - O SVM, por outro lado, poderia se beneficiar de um ajuste mais refinado dos hiperparâmetros ou até mesmo de uma abordagem diferente para lidar com esse tipo de dado.

### **2.4 Modelagem para Classificação com MLP**

1. **Estrutura**: MLP com X camadas escondidas, ativação ReLU, otimizador Adam, taxa de aprendizado Y.

2. **Avaliação**: Acurácia, F1-Score, Matriz de Confusão.

3. **Classification Report**:

```
               precision    recall  f1-score   support

        Fair       0.88      0.88      0.88       335
        Good       0.73      0.65      0.69      1004
       Ideal       0.81      0.92      0.86      4292
     Premium       0.67      0.74      0.70      2775
   Very Good       0.56      0.38      0.45      2382

    accuracy                           0.73     10788
   macro avg       0.73      0.71      0.72     10788
weighted avg       0.71      0.73      0.71     10788

```

4. **Matriz de Confusão**:

   ![Matriz de Confusão MLP](./assets/MatrizConfusaoClassMLP.png)

5. **Considerações sobre a aplicação do MLP**

   - O MLP apresentou bom desempenho na classificação múltipla, com margens de melhoria para classes menos representadas.

## **3. Clusterizações com KMEANS e DBSCAN**

### **3.1 Algoritmo de Estimativa KMEANS**

2. **Análise KMENS**

   - Inicialmente, foi adotado o KMeans com a preparação de features representam em porcentagem a profundidade e o diâmetro médio do diamente, respectivamente:

   ```
   features = ["depth", "table"]`
   ```

   ![Clusterização com K=5 ](./assets/Clusters5.png)

   - Foram apresentados, para análises, os gráficos de Inércia X Clusters ($k$), bem como a métrica silhouette_score para cada um dos agrupamentos $k$:

   ```
   k = [2, 3, 4, 5, 6, 7, 8]

   ```

   ![Cotovelo variando K ](./assets/CotoveloTeste.png)

   - Considerando que a métrica inércia demonstra a dispersão dentro dos clusteres (quanto menos melhor) e a silhouette avalia a qualidade dos clusteres (entre -1 e 1, quanto maior, mais agrupados), os primeiros resultados apontaram:

   ![Clusterização com K=5 ](./assets/Silhueta5.png)

   - Apesar de resultados diversos, consideramos os ajustes para comparações com os 5 tipos de features:

   ```
   k=5, para uma
   inércia = 31935.241437036213
   silhueta média = 0.38
   'cut' = Fair (Regular), Good (Bom), Very Good (Muito Bom), Premium, Ideal
   ```

   - A tabela abaixo representa uma comparação entre a feature `cut`, o label predito `labels_` e as categorias mencionadas:

| **cut/labels\_**        | **Fair** | **Good** | **Ideal** | **Premium** | **Very Good** | **Total por cluster** | **Ajuste (%)** | **Erros**     |
| ----------------------- | -------- | -------- | --------- | ----------- | ------------- | --------------------- | -------------- | ------------- |
| **0**                   | 43       | 321      | 5040      | 3675        | 2415          | 11494                 | 43.85          | 6454          |
| **1**                   | 37       | 430      | 13516     | 4869        | 3967          | 22819                 | 59.23          | 9303          |
| **2**                   | 130      | 475      | 1673      | 2127        | 1317          | 5722                  | 37.17          | 3595          |
| **3**                   | 1140     | 2709     | 250       | 230         | 2310          | 6639                  | 40.80          | 3930          |
| **4**                   | 260      | 971      | 1072      | 2890        | 2073          | 7266                  | 39.77          | 4376          |
| **Total por categoria** | 1610     | 4906     | 21551     | 13791       | 12082         | 53940                 | Não se aplica  | Não se aplica |

2. **Considerações sobre a aplicação do KMENS**
   - Avalia-se que para as `features = ["depth", "table"]`, os agrupamentos se esplalham nas categoria, ajustando-se de forma precária.

### **3.2 Algoritmo de Estimativa DBSCAN**

1. **Análise com DBSCAN**

   - Para a análise com o _DBSCAN_, foi feito duas analises distintas. Uma com a base original completa e outra com os dados pré tratados do `cleaned.csv`.

   - A base original requer alguns tratamentos, então foi selecionado as seguintes features como parte do modelo:

   ```
   features_numericas = ['depth', 'table', 'price']
   features_ordinais = ['color', 'cut', 'clarity']
   ```

   - Foi utilizado o _StandardScaler_ nas features numéricas e o _OrdinalEncoder_ nas fetures ordinais.

   - Na sequência foi feito um preprocessador com ColumnTransformer e as features e encoders adequados.

   - Esse preprocessador foi utilizado junto com o DBSCAN em um pipeline, na qual pode-se extrair o resultado dos labels de clusters.

   ```
   labels = dbscan_pipeline.named_steps['dbscan'].labels_
   df['cluster'] = labels
   ```

   - A partir dos labels conseguimos o seguinte gráfico:

   ![Clusters do DBSCAN com DataSet Completo](./assets/ClusterDBSCAN.png)

   - Após a primeira tentativa, utilizou-se o método _NearestNeighbors_ para estimar um melhor valor de eps, um dos hiperparâmetros do DBSCAN, com o seguinte resultado:

   ![Teste do Cotovelo](./assets/CotoveloDBSCAN.png)

   - Esse gráfico foi plotado com a escala de 0.00 até 2.00, que era onde estava o cotovelo, para melhor vizualização do ponto.O EPS selecionado foi o de 1.0.

   - O método da silhoueta foi utilizado como seleção de parâmetros também, porém o resultado obtido não pareceu fazer sentido, com valor negativo e constante.

   - A partir daí, foi feita a mesma analise utilizando a base de dados já processada. E usando o resultado de eps da etapa anterior, obteve-se o seguinte resultado:

   ![Cluster do DBSCAN com o DataSet Limpo](./assets/ClusterDBSCANLimpo.png)

### **3.3 Considerações Finais sobre a Clusterização**

- A partir deste ponto, a pesquisa toma novos rumos com a definição de outros agrupamentos e a modelagem com estimadores DBSCan e HCA.

- As novas avaliações apresentaram os resultados promissores.

- Os resultados mais indicados com KMeans:

```
features = ['carat', 'cut', 'depth', 'table']
k = 6
inertia=1804.96
silhouette_score=0.64
```

![Clusterização com K=6 ](./assets/Silhueta6.png)

- Com DBScan os melhores resultados, filtrando os parâmetros que apresentam os melhores **silhouette_scores** para cada conjunto de hiperparâmetros:

| **eps** | **min_samples** | **n_clusters** | **noise** | **silhouette_score** |
| ------- | --------------- | -------------- | --------- | -------------------- |
| 0.5     | 4               | 4              | 41        | 0.7034               |
| 0.4     | 4               | 10             | 140       | 0.5238               |

- Essas condições de **eps** e **min_samples** geraram um bom equilíbrio entre a formação dos clusters e a consistência da análise.

- Por fim, considerando os limites da presente pesquisa, faz-se necessária uma continuidade de novas análises e modelagens para melhoria da predição.

---