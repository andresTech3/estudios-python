# poder hacer analisis de dato con mucha mayor porfesionalidad en python 
#? panda es una libreria para analisis de datos y mucho mas eficiente que paquete csv
#? para trabajar con analisis de datos utilizar jupity un entorno desarrollo diferente en vscode
import pandas as pd; 

df = pd.read_csv("archivos\\texto.csv"); # df = dataframe
df2 = pd.read_csv("archivos\\texto.csv");
#print(df)

#*ordenar los dataframe por la edad
df_ordenado = df.sort_values("edad")
# print(df_ordenado)

#* ordenando los dataframe por forma desendente
df_ordenado_desendente = df.sort_values("edad",ascending=False)
# print(df_ordenado_desendente )

#*concatenando los 2 dataframe
df_concatenado = pd.concat([df,df2])
# print(df_concatenado)

#*accediendo a las fila con head() y tail()
primer_fila = df.head(3) #obtenemos las primeras 3 filas con head()
print(primer_fila)

ultimas_fila = df.tail(3) #obtenemos las ultimas 3 filas
print(ultimas_fila)

##################################################################################################
#*obteniendo todos los datos de la columna nombre
nombre = df['nombre'] 
#print(nombre)

#* definir o redefinir los encabezados de la tabla
#? parametro names redefinimos los encabezados de la tabla
df = pd.read_csv("archivos\\texto.csv",names=["Name","LastName","Age"]); # df = dataframe
# print(df)

# cadena = "0123456789"
#?tecnica slicer podemos definir que nos de los datos del comienzo de un array hasta el final que indiquemos
# savemos el slicer es variable[filas:columnas]
# print(cadena[0:4]) 
# print(cadena[:])  traeme todos los elementos

#* accediendo a la cantidad de filas y columnas con shape
file_y_colum_total = df.shape
filas = file_y_colum_total[0] #accedemos a las filas 
colum = file_y_colum_total[1] #accedemos a las columnas
print(file_y_colum_total) 

#* obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)

#*accediendo a un elemento especifico del df con loc -> hacede por el nombre del valor
specific_loc = df.loc[2,"Age"] #? parametros(index de la fila, valor a obtener)

#* accediendo a un elemento especifico dol df con iloc -> acede por el indice de valor
specific_iloc = df.iloc[2,2] #? parametros(index de la fila, index valor a obtener)

#* accediendo a todas las fila de una columna
apellido = df.iloc[:,1] #? trayendo todos los elementos de la columna y la posicion colum que queramos
print(apellido)

#* accediendo a la fila 3 con loc
fila_3_loc = df.loc[2, :]
print(fila_3_loc)

#* accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2, :]
print(fila_3_iloc)

#* accediendo a filas con edad mayor a 20
maxFile = df.loc[df["Age"]>20,:]

print(maxFile)



