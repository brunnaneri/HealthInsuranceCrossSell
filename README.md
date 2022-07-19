# Health Insurance Cross-Sell

COLOCAR FOTO

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Observação:
Este projeto foi inspirado no desafio "Health Insurance Cross-Sell Prediction" publicado no Kaggle (https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction). Por isso, trata-se de um problema fictício, no entanto solucionado com passos e análises de um projeto real.

## 1.0 PROBLEMA DE NEGÓCIO

### 1.1 Descrição do Problema
A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

### 1.2 Objetivo

Com a solução, o time de vendas deve conseguir priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Assim, será necessário construir um modelo que prediz se o cliente estaria ou não interessado no seguro de automóvel.

Como resultado será entregue respostas às seguintes perguntas:

  1. Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.
  2. Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?
  3. E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas   conseguirá contatar?
  4. Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

## 2.0 PREMISSAS DO NEGÓCIO
Algumas premissas foram assumidas no projeto durante o desenvolvimento da solução, que foram:
- Considerar que o time de vendas usa o Google Sheets diariamente como ferramenta e por isso a solução deverá ser incorporada nele como forma de facilitar o acesso.
- A solução foi baseada no cenário em que o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

## 3.0 PLANEJAMENTO DA SOLUÇÃO

### 3.1 Produto Final
Será disponibilizada uma ferramenta no Google Sheets que ordena/ranke a lista de clientes repassada de acordo com a sua propensão de compra (assinatura do seguro), de forma que os clientes com maior propensão estejam alocados no início da lista.

### 3.2 Processo
Analisando problema de negócio observa-se que se trata de projeto de Learning to Rank (LTR), e para solucioná-lo as seguintes tarefas foram realizadas:

**1.0 Data Collect**
- Foram coletados os dados em base de dados AWS Cloud e no site do Kaggle.

**2.0 Data Description**
- As características dos dados foram analisadas brevemente observando:
  - Dimensões
  - Tipos
  - A presença de dados nulos 
  - Estatística descritiva.

**3.0 Feature Engineering**
Etapa que de criação de novas features (colunas) derivadas as originais e criação de hipóteses que serão avaliadas na etapa de análise exploratória dos dados.

**4.0 Exploratory Data Analysis (EDA)**
Essa etapa é de grande importância, nela ocorre a validação ou não das hipóteses de negócio que foram levantadas. 
A análise exploratória dos dados foi feita a partir dos seguintes passos:
- Análise Univarida: avaliando uma variável por vez.
- Análise Bivariada: 
  Nesse momento se faz a análise/validação das hipóteses levantas do passo anterior.
  É feita a análise entre a variável resposta e as variáveis/atributos que atuam sob essa variável reposta.
  
**5.0 Data Preparation**
Preparação dos dados de forma que possibilite um melhor aprendizado do modelo de ML a ser aplicado, visto que a maioria desses tem um melhor desempenho quando se tem dados numéricos e em mesma escala.
- Normalização: dados numéricos que tem distribuição normal.
- Reescala: dados numéricos que não tem distribuição normal.
- Transformação - Encoding: transformar dados categóricos em numéricos.

**6.0 Feature Selection**
A seleção de atributos tem o objetivo de identificar e selecionar variáveis que caracterizam bem o fenômeno e por isso são relevantes para o modelo. Para isso, foi utilizado o algoritmo Boruta  (https://github.com/scikit-learn-contrib/boruta_py) e comparado seu resultado com as análises feitas na etapa de EDA.

O algoritmos de machine learning foram treinados considerando as variáveis selecionadas nessa etapa.

**7.0 Machine Learning Modelling - Cross Validation e Hyperparameter Fine Tunning**
Nesta etapa foram avaliados diferentes algoritmos de modelos de machine learning de aprendizado supervisionado, sendo estes: KNN Classifier, Logistic Regression, XGBoost Classifier, Random Forest Classifier e Extra Trees Classifier.

Os modelos foram treinados utilizando a técnica de cross-validation a fim de reduzir o viés da seleção dos dados (teoria da amostragem), visto que foram utilizadas diferentes amostras dos dados, e também foi feito o ajuste dos parâmetros do modelo, de modo a encontrar o de melhor perfomance.

O método "predict_proba" (as probabilidades para o target) foi usado para classificar a lista de clientes e traçar as curvas de lift e ganha, além de calcular as métricas de precision e recall.
Com isso foi possível observar a capacidade de aprendeizado de cada modelo.

**8.0 Model Training**
- Os três modelos que obtiveram melhor performance foram colocados para treinados novamente utilizando todos os dados disponíveis
- Os parâmetros utiliziados forama os selecionados na etapa de fune tunning
- As performances foram avaliadas novamente e a fim de obter a capacidade de generalização dos modelos.
- Neste passo, as métricas de precision@k e recall@k foram calculadas para diferentes valores de k (10%, 20%, 30%).
- k é o número (ou porcentagem, neste caso) de linhas da classe 1 (aquelas que estão interessadas em seguro de veículo) no tabela de probabilidade ordenada.

**9.0 Performance do Negócio (Resultado Financeiro)**
- Responder as questões de negócio.
- Comparar resultados da lista aleatória com o da lista ordenada por propensão de compra (resultado do modelo).
- Traduzir a performance do modelo em resultados financeiros para a Insurance All.

**10.0 Deploy Modelo to Production**
- Criar a classe e API para publicação em produção.
- Testar localmente.
- Publicar modelo no Heroku Cloud.
- Criar App Script em Google Sheets para consultar o modelo em produção.
- Implementar botão que consulta a propensão de compra dos clientes no Google Sheets, e testar a solução.

### 3.3 Entrada

#### 3.3.1 Fonte de Dados
- Dados coletados de um Banco de Dados AWS Cloud e da plataforma Kaggle.

#### 3.3.2 Ferramentas
- Python 3.8.12;
- Jupyter Notebook;
- Git e Github;
- Coggle Mindmaps;
- Heroku Cloud;
- Algoritmos de Regressão e Classificação;
- Pacotes de Machine Learning sklearn e xgboost;
- BorutaPy (seleção de atributos);
- Flask - Python API's;
- Google Sheets Apps Script.

## 4.0 TOP 4 INSIGHTS
Durante a análise exploratória de dados, na etapa de validação das hipóteses, foram gerados insights ao time de negócio.

Insights são informações novas, ou que contrapõe crenças até então estabelecidas do time de negócios, que devem ser acionáveis e assim direcionar resultados futuros.

**H1 - Pessoas mais velhas têm mais interesse em adquirir seguro de carros.**
**Falso** - Observa-se uma tendência decrescente com o avançar da idade. No entanto, a faixa etária de 30-45 anos corresponde a de pessoas mais interessadas em adquirir seguro.
COLOCAR GRÁFICOS (boxplot, crostab e linha de tendencia)

**H2 - Pessoas que tem carros mais antigos são mais interessadas em ter seguro de carro.**
**Verdadeiro** - Proporcionalmente, pessoas que tem carros mais antigos são mais interessadas em ter seguro.

COLOCAR GRÁFICOAS

**H3 - Pessoas que já tiveram problemas com carro são mais interessadas em ter seguro de carro.**
**Verdadeiro** - Nota-se que pessoas que já tiveram um problema com carro demonstraram mais interesse em ter o seguro.
COLOCAR GRÁFICOS

**H4 - Pessoas que já tem seguro de carro são menos interessadas em adquirir o seguro.
**Verdadeiro** - Pessoas que já tem seguro de carro demonstraram menos interesse em adquirir o seguro.
COLOCAR GRÁFICOS


## 5.0 MODELO DE MACHINE LEARNING APLICADO

## 6.0 PERFORMANCE DO MODELO

## 7.0 RESULTADOS DO NEGÓCIO

## 8.0 CONCLUSÕES

## 9.0 PRÓXIMOS PASSOS

## 10.0 REFERÊNCIAS





































