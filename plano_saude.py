import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#carregando dataset
train_data = pd.read_csv('./src/datasets/Train_Data.csv')

#verificando se há valores nulos
#print(train_data.isnull().sum())
# age         0
# sex         0
# bmi         0
# smoker      0
# region      0
# children    0
# charges     0
# dtype: int64

#verificando informações do dataset
# print(train_data.info())

# RangeIndex: 3630 entries, 0 to 3629
# Data columns (total 7 columns):
#    Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   age       3630 non-null   float64
#  1   sex       3630 non-null   object 
#  2   bmi       3630 non-null   float64
#  3   smoker    3630 non-null   object 
#  4   region    3630 non-null   object 
#  5   children  3630 non-null   int64  
#  6   charges   3630 non-null   float64
# dtypes: float64(3), int64(1), object(3)


#descrevendo o dataset
# print(train_data.describe())

#               age          bmi     children       charges
# count  3630.000000  3630.000000  3630.000000   3630.000000
# mean     38.887036    30.629652     2.503581  12784.808644
# std      12.151029     5.441307     1.712568  10746.166743
# min      18.000000    15.960000     0.000000   1121.873900
# 25%      29.000000    26.694526     1.000000   5654.818262
# 50%      39.170922    30.200000     3.000000   9443.807222
# 75%      48.343281    34.100000     4.000000  14680.407505
# max      64.000000    53.130000     5.000000  63770.428010 

#  

#          sex smoker     region
# count   3630   3630       3630
# unique     2      2          4
# top     male     no  southeast
# freq    2029   3070       1021

#Histograma
# plt.figure(figsize=(8,5))
# sns.histplot(train_data['charges'], kde = True)
# plt.title('Despesas com plano de saúde', fontsize=20)
# plt.show()

#boxplot para verificar se há outliers
# plt.figure(figsize=(8,5))
# sns.boxplot(train_data['charges'])
# plt.title('Despesas com plano de saúde (outliers)', fontsize=20)
# plt.show()

# histograma idade
# plt.figure(figsize=(8,5))
# sns.histplot(train_data['age'], kde=True)
# plt.title('Idade', fontsize = 20)
# plt.show()

#boxplot idade
# plt.figure(figsize=(8,5))
# sns.boxplot(train_data['age'])
# plt.title('Idade', fontsize = 20)
# plt.show()

# histograma imc
# plt.figure(figsize=(8,5))
# sns.histplot(train_data['bmi'], kde=True)
# plt.title('IMC', fontsize = 20)
# plt.show()

#boxplot imc
# plt.figure(figsize=(8,5))
# sns.boxplot(train_data['bmi'])
# plt.title('IMC', fontsize = 20)
# plt.show()

#histograma de qtd filhos
# plt.figure(figsize=(8,5))
# sns.histplot(train_data['children'], kde = True)
# plt.title('Quantidade de filhos', fontsize = 20)

#Boxplot de qtd filhos
# plt.figure(figsize=(8,5))
# sns.boxplot(train_data['children'])
# plt.title('Quantidade de filhos', fontsize = 20)

#Arredondando valores
train_data['age'] = round(train_data['age'])
train_data['age'] = round(train_data['age'])
# print(train_data.head())

#Usando OHEncoding para transformar as variáveis não numéricas em variáveis numericas
train_data = pd.get_dummies(train_data, drop_first=True)
# print(train_data.head(2))

#Separando as colunas que serao usadas
train_data = train_data[['age','sex_male', 'smoker_yes','bmi','children','region_northwest','region_southeast','region_southwest','charges']]
# print(train_data.head(2)) 
#Variaveis
x = train_data.iloc[:, :-1]
y = train_data.iloc[:, -1 ]
# print(y.head(2))

#Treino
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)