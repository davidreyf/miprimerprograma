import pandas as pd
import numpy as np
import random
import string
from tqdm import tqdm

filas = 50000
columnas = 3

df = pd.DataFrame(np.zeros((filas,columnas), dtype=object), columns=['col1', 'col2', 'col3'])
for i in range(filas):
    for j in range(columnas):
        df.iloc[i,j] = random.choice([chr(i) for i in range(33, 127)])

for row in tqdm(df.values,total=df.shape[0]):
        print(row)
        print(row[0])
   
    








