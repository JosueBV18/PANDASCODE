#!/usr/bin/env python3

import pandas as pd

print('__________________________________________________________________________________ \n')
print('Clase 03- CASE STUDY: MOVIES DATA ANAYSIS')
# print('__________________________________________________________________________________')
# print('MOVIES DATASET')
# movies = pd.read_csv('movies.csv')

# print(movies.head(2))
# print(movies.columns)
# print(movies.index)
# print(movies.shape)
# print('_________________________________________')
# print('TAGS DATASET')
# tags = pd.read_csv('tags.csv')

# print(tags.head(2))
# print(tags.columns)
# print(tags.index)
# print(tags.shape)
# print('_________________________________________')
# print('RATINGS DATASET')
# ratings = pd.read_csv('ratings.csv')

# print(ratings.head(2))
# print(ratings.columns)
# print(ratings.index)
# print(ratings.shape)

# print('__________________________________________________________________________________\n')
tags = pd.read_csv('tags.csv')
ratings = pd.read_csv('ratings.csv')
del ratings['timestamp']
del tags['timestamp']
print('__________________________________________________________________________________')
print('MOVIES DATASET')
movies = pd.read_csv('movies.csv')
print(movies.head(2))
print('__________________________________________________________________________________')
print('TAGS DATASET')
print(tags.head(2))
print('__________________________________________________________________________________')
print('RATINGS DATASET')
print(ratings.head(2))
print('__________________________________________________________________________________\n')
# print(tags.iloc[[0,11,2000]])
# print('Primeras 5 muestras')
# print(ratings.head())
# print('Ultimas 5 muestras')
# print(ratings.tail())
# print('__________________________________________________________________________________')
# # statistics = ratings['rating'].describe()
# # print(statistics)
# print('PROMEDIO')
# print(ratings['rating'].mean())
# print('MINIMO')
# print(ratings['rating'].min())
# print('MAXIMO')
# print(ratings['rating'].max())
# print('MODA')
# print(ratings['rating'].mode())
# print('MEDIANA')
# print(ratings['rating'].median())
# print('__________________________________________________________________________________')
print('FILTROS')
filter = ratings['rating']>5
print(filter.any())
filter02 = ratings['rating']>0
print(filter02.any())
print('__________________________________________________________________________________')
print('Verificar si existen valores nulos')
print('MOVIES')
print(movies.shape)
print(movies.isnull().any())
print('\n TAGS')
print(tags.shape)
print(tags.isnull().any())
print('\n RATINGS')
print(ratings.shape)
print(ratings.isnull().any())

#En caso que existen datos nulos borrar
# tags = tags.dropna()

#Visualizar los datos
print('__________________________________________________________________________________')
print('\n VISUALIZAR LOS DATOS')
import matplotlib.pyplot as plt

ratings.hist(column='rating', figsize=(5,7), color='green', edgecolor='black')
plt.show()

print('__________________________________________________________________________________')