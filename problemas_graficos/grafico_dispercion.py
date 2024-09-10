import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("problemas_graficos\\dispercion.csv")

#% barplot -> trabajar con grafico de dispercion
sns.scatterplot(x="tiempo", y="dinero", data=df)
sns.lineplot(x="tiempo", y="dinero", data=df)

plt.show()