import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("problemas_graficos\\bigotes.csv")

#% barplot -> trabajar con grafico de dispercion
sns.scatterplot(x="categoria", y="valor", data=df)
sns.lineplot(x="categoria", y="valor", data=df)



plt.show()