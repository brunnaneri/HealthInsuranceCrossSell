# Health Insurance Cross-Sell

<img src="https://github.com/brunnaneri/health_insurance_cross_sell/blob/main/images/vehicle-insurance.jpg?raw=true" width=70% height=70% title="Health-Insurance-Ranking" alt="project_cover_image"/>

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
Será disponibilizada uma ferramenta no Google Sheets que ordena/rankea a lista de clientes repassada de acordo com a sua propensão de compra (assinatura do seguro), de forma que os clientes com maior propensão estejam alocados no início da lista.

### 3.2 Processo
Analisando problema de negócio observa-se que se trata de um projeto de Learning to Rank (LTR), e para solucioná-lo as seguintes tarefas foram realizadas:

#### PASSO 1 - Data Collect
- Foram coletados os dados em base de dados AWS Cloud (utilizados para treino, validação e teste) e no site do Kaggle (para testar o modelo em produção).

#### PASSO 2 - Data Description
- As características dos dados foram analisadas brevemente observando:
  - Dimensões
  - Tipos
  - A presença de dados nulos 
  - Estatística descritiva.

#### PASSO 3 - Feature Engineering
Etapa de criação de novas features (colunas) derivadas as originais e criação de hipóteses que serão avaliadas na etapa de análise exploratória dos dados.

#### PASSO 4 - Exploratory Data Analysis (EDA)
Essa etapa é de grande importância, nela ocorre a validação ou não das hipóteses de negócio que foram levantadas. 
A análise exploratória dos dados foi feita a partir dos seguintes passos:
- Análise Univarida: avaliando uma variável por vez.
- Análise Bivariada: 
  Nesse momento se faz a análise/validação das hipóteses levantas do passo anterior.
  É feita a análise entre a variável resposta e as variáveis/atributos que atuam sob essa variável reposta.
  
#### PASSO 5 - Data Preparation
Preparação dos dados de forma que possibilite um melhor aprendizado do modelo de ML a ser aplicado, visto que a maioria desses tem um melhor desempenho quando se tem dados numéricos e em mesma escala.
- Normalização: dados numéricos que tem distribuição normal.
- Reescala: dados numéricos que não tem distribuição normal.
- Transformação - Encoding: transformar dados categóricos em numéricos.

#### PASSO 6 - Feature Selection
A seleção de atributos tem o objetivo de identificar e selecionar variáveis que caracterizam bem o fenômeno e por isso são relevantes para o modelo. Para isso, foi utilizado o algoritmo Boruta  (https://github.com/scikit-learn-contrib/boruta_py) e comparado seu resultado com as análises feitas na etapa de EDA.

O algoritmos de machine learning foram treinados considerando as variáveis selecionadas nessa etapa.

#### PASSO 7 - Machine Learning Modelling - Cross Validation e Hyperparameter Fine Tunning
Nesta etapa foram avaliados diferentes algoritmos de classificaçãao de modelos de machine learning de aprendizado supervisionado, sendo estes: KNN Classifier, Logistic Regression, XGBoost Classifier, Random Forest Classifier e Extra Trees Classifier.

Os modelos foram treinados utilizando a técnica de cross-validation a fim de reduzir o viés da seleção dos dados (teoria da amostragem), visto que foram utilizadas diferentes amostras dos dados, e também foi feito o ajuste dos parâmetros do modelo, de modo a encontrar o de melhor perfomance.

O método "predict_proba" (as probabilidades para o target) foi usado para classificar a lista de clientes e traçar as curvas de lift e ganho, além de calcular as métricas de precision e recall.
Com isso foi possível observar a capacidade de aprendizado de cada modelo.

#### PASSO 8 - Model Training
- Os três modelos que obtiveram melhor performance foram treinados novamente utilizando todos os dados disponíveis
- Os parâmetros utilizados foram os selecionados na etapa de fune tunning
- As performances foram avaliadas novamente a fim de se obter a capacidade de generalização dos modelos.
- Neste passo, as métricas de precision@k e recall@k foram calculadas para diferentes valores de k (10%, 20%, 30%).
- k corresponde ao número (ou porcentagem, neste caso) de linhas da classe 1 (aquelas que estão interessadas no seguro de veículo) no tabela de probabilidade ordenada.

#### PASSO 9 - Performance do Negócio (Resultado Financeiro)
- Responder as questões de negócio.
- Comparar resultados da lista aleatória com o da lista ordenada por propensão de compra (resultado do modelo).
- Traduzir a performance do modelo em resultados financeiros para a Insurance All.

#### PASSO 10 - Deploy Modelo to Production
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
- Algoritmos de Regressão e Classificação;
- Pacotes de Machine Learning sklearn e xgboost;
- BorutaPy (seleção de atributos);
- Flask - Python API's;
- Google Sheets Apps Script;
- Git e Github;
- Heroku Cloud;
- Coggle Mindmaps.

## 4.0 TOP 4 INSIGHTS
Durante a análise exploratória de dados, na etapa de validação das hipóteses, foram gerados insights ao time de negócio.

Insights são informações novas, ou que contrapõe crenças até então estabelecidas do time de negócios, que devem ser acionáveis e assim direcionar resultados futuros.

**H1 - Pessoas mais velhas têm mais interesse em adquirir seguro de carros.**
### Falso - Observa-se uma tendência decrescente com o avançar da idade. No entanto, a faixa etária de 30-45 anos corresponde a de pessoas mais interessadas em adquirir seguro.

![image](https://user-images.githubusercontent.com/101215927/179863850-93e69ac0-2d40-4814-8139-1f98cf4e83a4.png)

![image](https://user-images.githubusercontent.com/101215927/179863919-b03736b6-a3d7-4c81-a2f0-64b4b890261b.png)


**H2 - Pessoas que tem carros mais antigos são mais interessadas em ter seguro de carro.**
### Verdadeiro - Proporcionalmente, pessoas que tem carros mais antigos são mais interessadas em ter seguro.

![image](https://user-images.githubusercontent.com/101215927/179864111-b0baf444-d465-4cae-bfb1-d50f53de000a.png)

a = < 1 Year | b = 1-2 Year | c = >2 Year

**H3 - Pessoas que já tiveram problemas com carro são mais interessadas em ter seguro de carro.**
### Verdadeiro - Nota-se que pessoas que já tiveram um problema com carro demonstraram mais interesse em ter o seguro.

![image](https://user-images.githubusercontent.com/101215927/179864570-91cde153-f821-49c1-b579-4cf43c49f3d5.png)


**H4 - Pessoas que já tem seguro de carro são menos interessadas em adquirir o seguro.**
### Verdadeiro - Pessoas que já tem seguro de carro demonstraram menos interesse em adquirir o seguro.

![image](https://user-images.githubusercontent.com/101215927/179864616-372b7ef1-c736-4ee1-b455-bce3b5623e54.png)


## 5.0 MODELO DE MACHINE LEARNING APLICADO
Os modelos treinados, utilizando as técnicas de cross-validation e fine tunning, foram comparados através das métricas de precision e recall que obtiveram com a combinação de hyperparametros que teve melhor desempenho. Na tabela a seguir estão os valores médios dessas métricas e seu desvio padrão.

|Model|Precision|Recall
|:----------------|:------------------:|-----------------------:|
| KNN| 0.27355+/-0.00151 | 0.73199+/-0.00404  |
| L_Regression  | 0.29578+/-0.00117| 0.79116+/-0.00513 |
| XGB   | 0.29578+/-0.00117 | 0.8323+/-0.00316 |
| R_Forest| 0.29578+/-0.00117 |0.82257+/-0.00523|
| E_Trees| 0.30208+/-0.00116 | 0.80834+/-0.0031 |

A partir desses resultados, observou-se que os modelos XGBoost Classifier, Extra Tress Classifier e Random Forest Classifier obtiveram melhor desempenho, e seguiram para serem novamente treinados, desta vez utilizando todo o conjunto de dados de treino e o conjunto de parâmetros que apresentou melhor ajuste. O modelo foi testado no conjunto de dados de validação que foi separado na sessão 6.1, assim foi possível verificar a **capacidade de aprendizado do modelo**.

As métricas de recall@k e precision@k foram calculadas novamente, agora para diferentes valores de k e as curvas de lift e ganho foi plotadas e também confrontadas, observe a seguir.

![image](https://user-images.githubusercontent.com/101215927/179769647-13cb4083-1a1c-4241-ae54-5b936fd82ed7.png)

![image](https://user-images.githubusercontent.com/101215927/179769794-89ba6fc5-d60b-4b82-8efe-3d575815f93a.png)

|Precision@k| Xgboost Classifier |Random Forest Classifier |Extra Trees Classifier|
|----------------|:----------:|:-------------------:|:---------------------------------:|
| 10% (3049) | 0.400| 0.396 | 0.369 |
| 20% (6098) | 0.357 | 0.348 | 0.339 |
| 30% (9147) | 0.322 | 0.316 | 0.311 |


|Recall@k| Xgboost Classifier |Random Forest Classifier |Extra Trees Classifier|
|----------------|:----------:|:-------------------:|:---------------------------------:|
| 10% (3049) | 0.325 | 0.322 | 0.301 |
| 20% (6098) | 0.582 | 0.567 | 0.552 |
| 30% (9147) | 0.788 | 0.773 | 0.761 |


Com isso, pode-se confirmar o melhor desempenho do XGBoost Classifier e designá-lo para testar como modelo final e em seguida colocar em produção.

Para isso, o modelo foi novamente treinado, porém agora, unindo os dados de treino e validação utilizados anteriormente e testando o modelo com os dados de teste separados na sessão 1.2, e desse modo foi verificado a **capacidade de generalização do modelo**, a qual pode ser observada nas métricas a seguir:

|Precision@k| Xgboost Classifier Train |Xgboost Classifier Test |
|----------------|:----------:|:---------------------------------:|
| 10% | 0.400 | 0.390 |
| 20% | 0.357 | 0.352 |
| 30% | 0.322 | 0.318 | 

|Recall@k| Xgboost Classifier Train |Xgboost Classifier Test |
|----------------|:----------:|:---------------------------------:|
| 10% | 0.325 | 0.318 |
| 20% | 0.582 | 0.574 |
| 30% | 0.788 | 0.777 |

Nota-se que o modelo continuou performando bem e com métricas muito similares as obtidas anteriormente. Assim, o XGBoost Classifier foi treinado com toda a base de dados disponível e colocado em produção.


## 6.0 PERFORMANCE DO MODELO
As curvas de ganho e lift permitem verificar o bom desempenho do modelo. 

**Cumulative gain curve**: ordenada por propensão de compra, relaciona a porcentagem do total de clientes (x) com a porcentagem do total de clientes que estão interessados/propensos a comprar (y).
    
**Lift curve**: é derivada da curva de ganho; os valores no eixo y correspondem à razão da curva de ganho em relação a baseline (ordenação aleatória) e o eixo x corresponde o percentual da base de clientes. Portanto, informa o quanto o modelo é melhor que lista aleatória.

A seguir se pode observar a curvas obtidas com o modelo final XGBoost Classifier. 

![image](https://user-images.githubusercontent.com/101215927/179869785-77d6520e-ce16-40e5-a167-0f31b3ae6d2f.png)
![image](https://user-images.githubusercontent.com/101215927/179869794-0d7d6bce-faef-4daf-a3fa-efc3f3e2a3ed.png)

Através da curva de ganho verifica-se que em 40% da base de clientes estão inclusos mais de 80% do total de clientes interessados. Esse resultado é mais de 2x melhor que o baseline, esta relação está posta na curva de lift. 

O modelo foi pubicado no Heroku Cloud (https://www.heroku.com/) e disponibilizado para o time de vendas numa planilha no Google Sheets (https://docs.google.com/spreadsheets/d/13CCxxC_E1_ihTFkELHAXVpEJL2tH35sLbGaDbn_WBvs/edit#gid=0)

Qualquer funcionário da empresa consegue utilizar a planilha e estabelecer um ranking dos clientes com maior probabilidade de adquirir o seguro do veículo, utilizando o modelo em produção.

Como pode ser visto na demonstração abaixo, existe um botão que, uma vez ativado, após alguns segundos, retorna a lista já ordenada pelos clientes com maior probabilidade de adquirir o novo produto.

<img src="https://github.com/brunnaneri/health_insurance_cross_sell/blob/main/images/gif_sheets.gif" alt="cumulative gains curve and lift curve" title="cumulative gains curve and lift curve" align="center" height="500" class="center"/>


## 7.0 RESULTADOS DO NEGÓCIO

Respondendo as questões de negócio realizadas no início do projeto, tem-se:

- Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?

Considerando os 127 mil novos clientes selecionados pelo time de produtos, os quais não responderam a pesquisa para participar da campanha, tem-se que 20000        representa: 15.75% desse total.

Desse modo, considerando que a performance do modelo se manterá para os próximos cenários, analisando a curva de ganho e a coluna de predict score acumulada, é possível afirmar que cerca de 47% do total de clientes interessados estarão contidos nos 20mil clientes que serão contatados seguindo a lista de rankeamento obtida com o modelo.

No caso de uma lista não rankeada, uma random list, observa-se, neste caso, que seria possível contatar apenas 15.75% (baseline). Portanto, o modelo proposto supera o baseline em aproximadamente: 3.01 vezes.

Outros cenários foram explorados e estão descritos no notebook.

####  Resultados Financeiros 
Considerando um cenário em que a base de clientes a ser contatada é a que está sendo utilizada nos dados de teste, que contabiliza: 76222 clientes, é possível estimar o retorno financeiro que a empresa terá ao utilizar a lista rankeada para entrar em contato com os clientes.

Inicialmente, serão consideradas algumas premissas para este cenário:

- Será considerado que o valor anual médio do seguro de carro é igual ao valor anual médio do seguro de sáude desta empresa, que é de 30556.68.
- Será assumido que as pessoas que respoderam estar interessadas no seguro irão efetivamente adquiri-lo.

Nesta base de 76222 clientes tem-se 9388 clientes que estão interessados no seguro.
 
 Consultando o resultado do modelo, com a lista rankeada, observa-se que no ranking 20000 estão contidos aproximadamente 72.02% destes clientes interessados no seguro, que corresponde a 6761 clientes.
 
No caso da random list, contatando os 20000 clientes apenas 26.24% dos clientes interessados estariam entre esses, que corresponde a 2463 clientes.
- É possível observar essas relações na curve de ganho acumulativo analisando as intercções com a linha verde, que aparece a seguir:

![image](https://user-images.githubusercontent.com/101215927/179783747-9a1612e4-d449-4d60-8873-c0929bab9f49.png)

Desse modo, a receita bruta esperada através dos seguros vendidos aos clientes contatados utilizando a lista rankeada é de: **$206593713.48**. Enquanto que  utilizando a random list é de: **$75261102.84**.

Portanto, **o modelo é cerca de 2.75x melhor que a random list**.

- Essa relação está posta na curva de lift (ver intercções com a linha verde):
![image](https://user-images.githubusercontent.com/101215927/179783920-d21f23f0-c09b-4af6-811b-33e905d3ab24.png)


## 8.0 CONCLUSÕES

Com o resultado obtido é razoável considerar que o projeto foi bem sucedido, visto que a eficiência do modelo mais que dobrou o alcance do time de vendas em contatar os clientes interessados considerando o limite da campanha, que foi de 20 mil ligações.

Espera-se que o modelo em produção continue com essa performance na predição para dados de novos clientes, e desse modo o acesso a predição via planilha favorecerá a prospecção de novos clientes, atrelado a uma redução de custo e consequentemente aumento de faturamento pela empresa.

Além disso, com os insights tirados do estudo e bom aproveitamento da planilha criada, que possibilita simular clientes e suas características e com isso obter sua propensão de compra, é possível direcionar campanhas de marketing e aquisição de novos clientes com base nessas informações.

## 9.0 PRÓXIMOS PASSOS
Para um próximo ciclo CRISP, pode-se considerar:

- Estudar a necessidade/possibilidade de balancear os dados;
- Treinar diferentes modelos de classificação.

## 10.0 REFERÊNCIAS

- Dataset e problema obtidos no Kaggle (https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)
- https://medium.com/@m_n_malaeb/recall-and-precision-at-k-for-recommender-systems-618483226c54
- https://medium.com/turing-talks/como-avaliar-seu-modelo-de-classifica%C3%A7%C3%A3o-acd2a03690e

