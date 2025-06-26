#!/usr/bin/env python3

import pandas as pd

import matplotlib.pyplot as plt

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
#print(movies.head(2))
print('__________________________________________________________________________________')
print('TAGS DATASET')
#print(tags.head(2))
print('__________________________________________________________________________________')
print('RATINGS DATASET')
#print(ratings.head(2))
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
# print('FILTROS')
# filter = ratings['rating']>5
# print(filter.any())
# filter02 = ratings['rating']>0
# print(filter02.any())
# print('__________________________________________________________________________________')
# print('Verificar si existen valores nulos')
# print('MOVIES')
# print(movies.shape)
# print(movies.isnull().any())
# print('\n TAGS')
# print(tags.shape)
# print(tags.isnull().any())
# print('\n RATINGS')
# print(ratings.shape)
# print(ratings.isnull().any())

#En caso que existen datos nulos borrar
# tags = tags.dropna()

#Visualizar los datos
# print('__________________________________________________________________________________')
# print('\n VISUALIZAR LOS DATOS')


# ratings.hist(column='rating', figsize=(5,7), color='green', edgecolor='black')
# plt.show()

# print('__________________________________________________________________________________\n')

# print(tags.head(3))
# tagstwovariables = tags[['movieId','tag']]
# print('\n',tagstwovariables.head(5))

# print('\n',tagstwovariables.shape)

# simplerang = ratings[1000:1020]
# print('\n', simplerang.shape)
# print('\n',simplerang.head(2))

# print('Contar el numero de etiquetas que se repiten')
# tags_counts = tags['tag'].value_counts()
# print(tags_counts.shape)
# print(tags_counts[:10])

# # tags_counts[:10].plot(kind='bar', figsize=[15,10], color='green', edgecolor='purple')
# # plt.show()

# print('\n',ratings.head(2))
# is_highly_rated = ratings['rating']>=4
# print(is_highly_rated.shape)
# is_highly_rated_df = ratings[is_highly_rated]
# print(is_highly_rated_df.shape)

# print('\n',movies.head(10))
# print(movies.shape)
# is_genres = movies['genres'].str.contains('Animation', case=False, na=False)
# is_genres_df = movies[is_genres]
# print('\n', is_genres_df.head(10))
# print(is_genres.shape)

print('AGRUPAR')
print('__________________________________________________________________________________\n')

agroup_rating = ratings[['movieId', 'rating']].groupby('rating').count()
print(agroup_rating)
print(agroup_rating.shape)
agroup_rating[:10].plot(kind='bar', figsize=[15,10], color='green', edgecolor='purple')
plt.show()

raten_rating = ratings[['movieId', 'rating']].groupby('movieId').mean()
print(raten_rating.head(10))
print(raten_rating.shape)

raten_rating_Id = ratings[['movieId', 'rating']].groupby('movieId').count()
print(raten_rating_Id.head(10))
print(raten_rating_Id.shape)

print('__________________________________________________________________________________')