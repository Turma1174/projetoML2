### PRINCIPAIS RESULTADOS DO PROJETO DIAMONDS

---

### **1.1 Origem e Motivação do Dataset**

- **Origem:** O *dataset diamonds* está disponível no Kaggle e faz parte do pacote `ggplot2` em R. Ele foi construído para exemplificar análises de regressão, visualização de dados e modelagem estatística.  

- **Motivação:** A ideia é ajudar estudantes e profissionais a explorar dados reais sobre diamantes, analisando como características (como quilates, corte e cor) influenciam o preço de mercado.  

---

### **1.2 Representatividade no Mercado de Diamantes**

- **Cenário:** O *dataset* contém mais de 53 mil registros e se baseia em métricas padrão do mercado (quilates, corte, cor, claridade e preço).  

- **Limitações:** Ele pode não capturar toda a dinâmica do mercado real, como flutuações de preços baseadas em demanda, sazonalidade ou negociações específicas. Além disso, os dados podem ser simplificados e não consideram fatores como origem ética ou certificação de procedência, que afetam o valor.  

- **Conclusão:** Ele é um bom ponto de partida para modelagem, mas precisaria de complementos para representar o mercado atual de forma mais robusta.  

---

### **1.3 Aspectos Importantes para Conferir no Dataset**

1. **Consistência dos dados:**  
   - Verificar se todas as variáveis estão bem preenchidas e sem valores ausentes.  
   - Identificar possíveis *outliers*, especialmente em preços e quilates.  
2. **Correlação entre variáveis:**  
   - Explorar a relação entre características físicas (como corte, cor, claridade) e o preço para confirmar se as tendências estão alinhadas com o mercado.  
3. **Distribuição dos dados:**  
   - Conferir a distribuição das variáveis contínuas (como quilates e preço) e categóricas (como corte e cor) para garantir que são representativas.  
4. **Qualidade da categorização:**  
   - Avaliar se as categorias de "cut", "color" e "clarity" estão claras e consistentes.

---

### **1.4 Novas Features a partir das Existentes**

- **Relação Preço x Quilates:** Criar uma feature com o preço por quilate para facilitar análises de custo-benefício.  
- **Interação entre Variáveis:**  
   - Combinar "cut", "color" e "clarity" em uma *feature* composta, como um índice de qualidade geral.  
   - Normalizar os preços para análise relativa dentro de categorias de corte.  
- **Clusters de Preços:** Utilizar técnicas como *k-means* para categorizar os diamantes em grupos de preços similares, facilitando análises segmentadas.  

---

### **1.5 Pontos Relevantes**

1. **Modelagem Apropriada:**  
   - O problema principal é prever o preço (variável contínua), então os modelos de regressão (linear, árvore de decisão, *random forest*, ou *gradient boosting*) seriam os mais indicados.  
2. **Análise de Feature Importance:**  
   - Utilizar técnicas como SHAP ou permutação de importância para verificar o impacto de cada variável no preço.  
3. **Engenharia de Dados:**  
   - Considerar transformar "cut", "color" e "clarity" em variáveis numéricas ou *embeddings* categóricos para melhorar o desempenho de modelos baseados em aprendizado profundo.  
4. **Validação e Testes:**  
   - Dividir os dados com atenção (por exemplo, *stratified splitting* para manter proporções entre categorias) e validar o modelo com métricas adequadas como RMSE ou MAE.

---

### **1.6 Considerações Finais**

1. **Quanto ao DataSet:**  
   - O DataSet não tinha nenhum problema de falta de dados, então a única alteração feita foi criar _bins_ para categorizar faixas de quilates.
   Após essa alteração

2. **Quanto aos algoritmos estimados e clusterizadores:**  
   - Inicialmente, foi adotado o KMeans com a preparação das `features = ["depth", "table"]`,  que representam em porcentagem a profundidade e o diâmetro médio do diamente, respectivamente;
   - Foram apresentados, para análises, os gráficos de Inércia X Clusters ($k$), onde `k = [2, 3, 4, 5, 6, 7, 8]`, bem como a métrica silhouette_score para cada um dos agrupamentos $k$;
   - Considerando que a métrica inércia demonstra a dispersão dentro dos clusteres (quanto menos melhor) e a silhouette avalia a qualidade dos clusteres (entre -1 e 1, quanto maior, mais agrupados), os primeiros resultados apontaram uma Inércia para clusterização com k = 6: 26834.2886326148.
   - Apesar dos resultados, mantemos k=5, para uma inercia de 31935.241437036213 e uma silhouette médio de 0.38, para ajustes e comparações com os 5 tipos de `'cut' = Fair (Regular), Good (Bom), Very Good (Muito Bom), Premium, Ideal`;
   - A tabela abaixo representa uma comparação entre a feature `cut`, o label predito `labels_` e as categorias mencionadas:

| **cut/labels_** | **Fair** | **Good** | **Ideal** | **Premium** | **Very Good** | **Total por cluster** | **Ajuste (%)** | **Erros** |  
|---------|----------|----------|-----------|-------------|---------------|-----------------------|----------------|-----------|  
| **0**   | 43       | 321      | 5040      | 3675        | 2415          | 11494                 | 43.85          | 6454      |  
| **1**   | 37       | 430      | 13516     | 4869        | 3967          | 22819                 | 59.23          | 9303      |  
| **2**   | 130      | 475      | 1673      | 2127        | 1317          | 5722                  | 37.17          | 3595      |  
| **3**   | 1140     | 2709     | 250       | 230         | 2310          | 6639                  | 40.80          | 3930      |  
| **4**   | 260      | 971      | 1072      | 2890        | 2073          | 7266                  | 39.77          | 4376      |  
| **Total por categoria** | 1610     | 4906     | 21551     | 13791       | 12082         | 53940                 | Não se aplica            | Não se aplica        |

   - Avalia-se que para as `features = ["depth", "table"]`, os agrupamentos se esplalham nas categoria, ajustando-se de forma precária.
   - A partir deste ponto, a pesquisa toma novos rumos com a definição de outros agrupamentos e a modelagem com estimadores como DBSCane e HCA.
   - Considerando os limites da presente pesquisa, as novas avaliações apresentaram os resultados abaixo:
   - Os resultados mais indicados com KMeans foram: `features = ['carat', 'cut', 'depth', 'table']`, com `(k = 6)`, `inertia=1804.96` e `silhouette_score=0.64`;
   - Com DBScan os melhores resultados, filtrando os parâmetros que apresentam os melhores **silhouette_scores** para cada conjunto de hiperparâmetros:

| **eps** | **min_samples** | **n_clusters** | **noise** | **silhouette_score** |
|---------|-----------------|----------------|-----------|----------------------|
| 0.5     | 4               | 4              | 41        | 0.7034               |
| 0.4     | 4               | 10             | 140       | 0.5238               |

   - Essas condições de **eps** e **min_samples** geraram um bom equilíbrio entre a formação dos clusters e a consistência da análise;
   - Por fim, considerando os limites da presente pesquisa, faz-se necessária uma continuidade de novas análises e modelagens para melhoria da predição;
   - Modelagem no arquivo clusterizacao_kmeans.ipynb e outros_teste.ipynb;

3. **Quantos às métricas do modelo:**  
   - ??????????????????? 

4. **Quanto às limitações de produção:**  
   - ???????????????????

4. **Agradecimentos:**  
   - ???????????????????

5. **Tecnicas de regressão:**  
   ## Tecnicas utilizadas
   - Bagging - Método que combina múltiplos modelos independentes para maior robustez.

Resultados:
 MSE: 294405.62
 R²: 0.98
 RMSE: 542.59

   - Boosting - Modelos sequenciais que corrigem erros do anterior, como Gradient Boosting e XGBoost.

Resultados:
 MSE: 280468.76
 R²: 0.98
 RMSE: 529.59

   - SVM - Modelagem que maximiza margens e explora diferentes kernels.

Resultados:
MSE: 6938259.41
R² Score: 0.56
RMSE: 2634.06

   - MLP Regressor - Rede neural ajustada para capturar relações complexas.

Resultados:
MSE: 335075.82
RMSE: 578.86
R² Score: 0.98


5. **Classificação multipla com MLP:**  
   ## Tecnicas utilizadas
   
   Estrutura: MLP com X camadas escondidas, ativação ReLU, otimizador Adam, taxa de aprendizado Y.

Avaliação: Acurácia, F1-Score, Matriz de Confusão.

Classification Report:
               precision    recall  f1-score   support

        Fair       0.88      0.88      0.88       335
        Good       0.73      0.65      0.69      1004
       Ideal       0.81      0.92      0.86      4292
     Premium       0.67      0.74      0.70      2775
   Very Good       0.56      0.38      0.45      2382

    accuracy                           0.73     10788
   macro avg       0.73      0.71      0.72     10788
weighted avg       0.71      0.73      0.71     10788



Matriz de Confusão: Espaço para matriz <-- está no codigo>
Conclusão
O MLP apresentou bom desempenho na classificação múltipla, com margens de melhoria para classes menos representadas.


# PARTE SOBRE DBSCAN - ELABORADA POR ANDRÉ FILIPE (alterar esse título)

Para a análise com o *DBSCAN*, foi feito duas analises distintas. Uma com a base original completa e outra com os dados pré tratados do `cleaned.csv`.

A base original requer alguns tratamentos, então foi selecionado as seguintes features como parte do modelo:

```
features_numericas = ['depth', 'table', 'price']
features_ordinais = ['color', 'cut', 'clarity']
```

Foi utilizado o *StandardScaler* nas features numéricas e o *OrdinalEncoder* nas fetures ordinais.

Na sequência foi feito um preprocessador com ColumnTransformer e as features e encoders adequados.

Esse preprocessador foi utilizado junto com o DBSCAN em um pipeline, na qual pode-se extrair o resultado dos labels de clusters.

```
labels = dbscan_pipeline.named_steps['dbscan'].labels_
df['cluster'] = labels
```

A partir dos labels conseguimos o seguinte gráfico
####Inserir gráfico `Clusters do DBSCAN com DataSet Completo` (apagar essa linha)

Após a primeira tentativa, utilizou-se o método *NearestNeighbors* para estimar um melhor valor de eps, um dos hiperparâmetros do DBSCAN, com o seguinte resultado:

####Inserir gráfico `Teste do Cotovelo` (apagar essa linha )

Esse gráfico foi plotado com a escala de 0.00 até 2.00, que era onde estava o cotovelo, para melhor vizualização do ponto.
O EPS selecionado foi o de 1.0.

O método da silhoueta foi utilizado como seleção de parâmetros também, porém o resultado obtido não pareceu fazer sentido, com valor negativo e constante.

A partir daí, foi feita a mesma analise utilizando a base de dados já processada.
E usando o resultado de eps da etapa anterior, obteve-se o seguinte resultado:

####Inserir gráfico `Cluster do DBSCAN com o DataSet Limpo` (apagar essa linha)