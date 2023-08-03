#filtrar por números:
import pandas as pd
datos = [10, 20, 30, 40, 50, 60]
#el indice, solo da una identificacion a los datos
indices = ['A', 'B', 'C', 'D', 'E', 'F']
s1 = pd.Series(datos, index=indices)

x = s1 [s1 > 30]
print(x)


#Filtrar por Strings:

import pandas as pd

#ponemos aqui los strings, proque necesitamos comparar con los strings y no con numeros.
datos = ['A', 'B', 'C', 'D', 'E', 'F']
#el indice, solo da una identificacion a los datos
indices = ['A', 'B', 'C', 'D', 'E', 'F']
s2 = pd.Series(datos, index=indices)
print(s2)

# Seleccionar los elementos con etiquetas alfabéticamente mayores que 'E'
x = s2[s2 > 'E']
print(x)

