import pandas as pd
import numpy as np
df_vacio =pd.DataFrame()
print(type(df_vacio)) 
data = {
        "Nombre":["Juan","Mary","Charles"],
        "Edad":[33,45,22],
        "Ciudad":["Madrid","Bilbo","Valencia"],
        }
df =pd.DataFrame(data)
print(df)
df.to_excel("excel.xlsx")
df1 = pd.read_excel("Animal.xlsx")
print(df1)

filas = 100
columnas = 3
data = np.random.rand(filas,columnas)
print(data)
df2 = pd.DataFrame(data,columns=["Penetración Iónica","Gamma","Impedancia"])
print(df2)
print(df2.head(15))
print(df2.tail(15))
print(df2.sample(15))
print(df2.info())
print(df2.describe())
print(df1.loc[1,"Animal"])
   
df1.loc[2,"Animal"] = "Elefante"   
print(df1)
df1["estatura"] = 999
print(df1)
df1["estatura"]= [122,121,111]
print(df1)
df1 = df1.append({"Animal":"Correcaminos","Edad": 8,"Peso": 876,"estatura": 321}, ignore_index=True)      
print(df1)
df_t = df1.T
print(df_t)
df_t.to_excel("df_transpuesto.xlsx")
df1["Edad"]= df1["Edad"].map(lambda x:x+1)
print(df1)