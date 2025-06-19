#!/usr/bin/env python3

import pandas as pd

# df=pd.read_csv('students_dirty_dataset_100.csv')

print('_______________________________________________________________________________________________________')

tags = pd.read_csv('tags.csv')
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# print('TAGS')
# print(tags.columns)
# print('RATINGS')
# print(ratings.columns)
# print('MOVIES')
# print(movies.columns)
# print('_______________________________________________________________________________________________________')

#Juntar Tablas
# print('MERGE DATAFRAMES')
# df = movies.merge(tags, on='movieId', how='inner')

# print('\n',df.columns)
# print(df.head(3))

print('_______________________________________________________________________________________________________')

print(ratings.head(5))
avg_ratings = ratings.groupby('movieId', as_index=False).mean()
print('\n',avg_ratings.head(5))

#ELiminar una columna
del avg_ratings['userId']
print('\n',avg_ratings.head(5))

print('_______________________________________________________________________________________________________')

df02 = movies.merge(avg_ratings, on='movieId', how='inner')
filter = df02['rating']>=4.0
print(df02.columns)
print('\n',df02[filter][-5:])

print('_______________________________________________________________________________________________________')
#Tranfoma a tiempo y hora
print(tags.columns)
print(tags['timestamp'].dtype)

tags['easytoreadforme']=pd.to_datetime(tags['timestamp'], unit='s')
print('\n',tags['easytoreadforme'].dtype)
print('\n',tags['easytoreadforme'][-5:])

print('\n', 'DF03')
greater_than_t = tags['easytoreadforme']>'2015-01-01'
df03 = tags[greater_than_t]
print(df03.shape)
print('\n', 'TAGS')
print(tags.shape)

print('_______________________________________________________________________________________________________')
