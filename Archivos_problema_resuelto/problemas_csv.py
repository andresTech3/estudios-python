import pandas as pd

df = pd.read_csv("archivos_problema_resuelto\\texto.csv")

#cambiar el tipo de dato a una fila

df['edad'] = df['edad'].astype(str)

#remplazar datos del csv
df['apellido'].replace("yemey", "jaramillo", inplace=True)
print(df)

#eliminando filas con datos faltantes
#df.dropna(axis=1) -> asi se elimina la columna con datos faltante
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante (limpio)
df.to_csv("archivos_problema_resuelto\\data_limpio.csv")
