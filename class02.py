
print('________________________________________________________________________________________________________________')
print('LOAD THE DATABASE')

import pandas as pd

df=pd.read_csv('students_dirty_dataset_100.csv')
# print(df.head(5))
# print(df.tail(5))
# print(df.shape)

# print('________________________________________________________________________________________________________________')
# print('EXPLORE THE DATASET')
# print(df.info())

# print('________________________________________________________________________________________________________________')
# print(df.describe(include='all'))

print('________________________________________________________________________________________________________________')
print('DETECT DATA QUALITY ISSUES')
print(df.isnull().sum())
# print('________________________________________________________________________________________________________________')
# print('DDUPLICATE')
# print(df.duplicated().sum())
# print(df['department'].value_counts())

print('________________________________________________________________________________________________________________')
#Completar datos con la media
print('HANDLE MISSING VALUES')

# Valores Numericos 

#Solucion para los datos nulos de age
# df['age'].fillna(df['age'].median(),inplace=True)
df['age'] = df['age'].fillna(df['age'].median())
#Solucion para los datos nulos de english_score
df['english_score'] = df['english_score'].fillna(df['english_score'].median())
#Solucion para los datos nulos de admission_year
df['admission_year'] = df['admission_year'].fillna(df['admission_year'].mode()[0]) #ELige el primero
#Solucion para los datos nulos de math_score
df['math_score'] = df['math_score'].fillna(df['math_score'].median())

# Valores Texto 
#Solucion para los datos nulos de gender
# df['gender'].fillna('Unknown',inplace=True)
df['gender'] = df['gender'].fillna('Unknown')

print(df.isnull().sum())

print('________________________________________________________________________________________________________________')
print('NORMALIZE CATEGORICAL VALUES')

df['department'] = df['department'].str.lower().str.strip()#Elimina los vavalores vacios al inicio y al final
