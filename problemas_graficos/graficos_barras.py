import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#% seaborn trabaja con graficos estadisticos

df = pd.read_csv("problemas_graficos\\coflaIngreso.csv")
print(df)

#% barplot -> trabajar con grafico de barras

sns.barplot(x="fuente", y="ingresos", data = df) 

plt.show() #? mostrar la graficas 