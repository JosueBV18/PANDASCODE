#!/usr/bin/env python3

import pandas as pd

print('_________________________________________ \n')
print('Clase 02- Pandas')
print('_________________________________________')
print('')

# ser = pd.Series(data=[1,2], index=['Josue','Miller'])

# print(ser.index)
# print('Luis' in ser)

# print('Before')
# print((ser))
# print('After')
# print(ser**2)

# ser02 = pd.Series(data=[100,200], index=['Camila','Jennifer'])
# print(ser02[['Camila']])

print('PANDAS DATAFRAME')

df = {'one':pd.Series(data=[100,200,300], index=['Pera','Manzana','Limon']),
      'two':pd.Series(data=[400,500,600], index=['Pera','Tomate','Limon'])}

df01 = pd.DataFrame(df)

# print(df01)

# print('Index {}'.format(df01.index))
# print('Columns', df01.columns)

df01['three']=df01['one']*df01['two']
print(df01)

df01['Flag']=df01['three']>200
print(df01)

aux01 = df01.pop('three')
print(df01)

df01.insert(2, 'Copy of two', df01['two'])
df01['FlagTwo']=df01['Copy of two']>200
aux02 = df01.pop('Copy of two')
print(df01)

df01['twoUpperHalf'] = df01['two'][:2]
print(df01)

df01['twoDonwHalf'] = df01['two'][2:]
print(df01)


print('')
print('_________________________________________')