
print('________________________________________________________')
print('LOAD THE DATABASE')

import pandas as pd

df=pd.read_csv('students_dirty_dataset_100.csv')
print(df.head(5))
print(df.tail(5))
print(df.shape)

print('________________________________________________________')
print('EXPLORE THE DATASET')
print(df.info())

print('________________________________________________________')
print(df.describe(include='all'))