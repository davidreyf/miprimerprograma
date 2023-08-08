import pandas as pd
#import dtale
from skimpy import skim

# URL del conjunto de datos Wine
url_wine = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

# Definir nombres de columnas para el DataFrame
column_names = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash',
                'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
                'proanthocyanins', 'color_intensity', 'hue', 'od280_od315_of_diluted_wines',
                'proline']

# Descargar el conjunto de datos y leerlo en un DataFrame
df_wine = pd.read_csv(url_wine, header=None, names=column_names)


# Visualizar las primeras filas del DataFrame
skim(df_wine)
print(skim(df_wine))
