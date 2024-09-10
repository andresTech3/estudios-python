import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#% seaborn trabaja con graficos estadisticos

df = pd.read_csv("problemas_graficos\\archivo.csv")
print(df)

#% lineplot -> trabajar con grafico de lineas
#% barplot -> trabajar con grafico de barras

sns.lineplot(x="fecha", y="organizar_cuarto", data = df) #? asignarle los ejes a las graficas con sus valores
sns.barplot(x="fecha", y="organizar_cuarto", data = df)

total_organizacion = df["organizar_cuarto"].sum() #% metodo que nos suma todos los datos de la columna selecionada


# plt.plot("01-12", 15, "o") #? plot para agregar punto en la graficas
plt.title(f'total de cuartos organizados : {total_organizacion}')

plt.show() #? mostrar la graficas 