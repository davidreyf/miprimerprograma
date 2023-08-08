#%%time

# %%time es una line magic function y sirve para contar el tiempo de ejecución de una celda de un cuaderno de Jupiter.

import pandas as pd
import random
import string
from tqdm import tqdm
import time

# Variable para concatenar los datos de todas las categorías 
all_characters = string.ascii_letters + string.digits + string.punctuation

num_rows = 1000
num_columns = 3

# Generar los datos utilizando caracteres aleatorios de todas las categorías
data = [[random.choice(all_characters) for _ in range(num_columns)] for _ in range(num_rows)]

# Crear un DataFrame con los datos generados
df = pd.DataFrame(data, columns=[f'Col{i+1}' for i in range(num_columns)])

# Imprimir el DataFrame
print(df)

print(df.shape[0]) #te da el numero de filas del dataframe



"""

FORMA 1: USANDO df.iterrows()

"""

# Ejemplo de bucle con tqdm para la barra de progreso
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    print("index",index)
    print("row",row)
    print("row['Col1']=", row['Col1'])



"""

FORMA 2: USANDO df.itertuples()

"""



# Ejemplo de bucle con tqdm para la barra de progreso
for row in tqdm(df.itertuples(), total=df.shape[0]):
    print("row",row)
    print("row.Col1")


"""

FORMA 3: USANDO df.values() para iterar sobre una lista

"""

# Ejemplo de bucle con tqdm para la barra de progreso
for row in tqdm(df.values, total=df.shape[0]):
    print("row:", row)
    print("row[0]:", row[0])


"""

FORMA 4: iterando sobre un diccionario 

"""
# Ejemplo de bucle con tqdm para la barra de progreso
df_dict = df.to_dict('records') #parámetros posibles: 'dict', 'list', 'series', 'split', 'records', 'index')
"""
El parámetro determina el tipo de valor del diccionario.

'dict' (default) : dict like {column -> {index -> value}}
'list' : dict like {column -> [values]}
'series' : dict like {column -> Series(values)}
'split' : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
'tight' : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values], ‘index_names’ -> [index.names], ‘column_names’ -> [column.names]}
'records' : list like [{column -> value}, … , {column -> value}]
'index' : dict like {index -> {column -> value}}

"""

# Ejemplo de bucle con tqdm
for row in tqdm(df_dict, total=df.shape[0]):
    print("row:", row)
    print("row['Col1']:", row['Col1'])

