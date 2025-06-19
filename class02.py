
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
print(df['department'].head(10))
print('________________________________________________________________________________________________________________')

df['department'] = df['department'].str.upper().str.strip()
print(df['department'].head(10))

print('________________________________________________________________________________________________________________')

print('remove duplicate')
df.drop_duplicates(inplace=True)
df.reset_index(drop=True,inplace=True)
print(df.shape)


print('________________________________________________________________________________________________________________')

print('create a new feature')
df['avr_score']=df[['math_score','english_score']].mean(axis=1)
print(df['avr_score'].head(10))
print('________________________________________________________________________________________________________________')
print(df.head(10))


print('________________________________________________________________________________________________________________')
print('display top performing students')
topstudensts=df.sort_values(by='avr_score',ascending=False).head(10)
print(topstudensts[['student_id','name','avr_score']])


print('________________________________________________________________________________________________________________')
print('export clean dateset')
df.to_csv('students_clean_dateset.csv', index=False)
print('ok')