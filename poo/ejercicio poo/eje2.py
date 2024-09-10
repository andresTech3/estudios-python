import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Graficos:
    def __init__(self, fileUrl):
        self.fileUrl = fileUrl
        self.df = pd.read_csv(self.fileUrl)
        sns.set_theme(style="whitegrid")
    
    def graficoBarra(self,valueX,valueY):
        sns.barplot(x= valueX, y= valueY, data= self.df)
        plt.show()

    def graficoLinea(self,valueX,valueY):
        sns.lineplot(x= valueX, y= valueY, data= self.df)
        plt.show()

    def graficoDispersion(self,valueX,valueY):
        sns.scatterplot(x= valueX, y= valueY, data= self.df)
        plt.show()

graficoTienda = Graficos("poo\\ejercicio poo\\ropaData.csv")
graficoIngresos = Graficos("problemas_graficos\\coflaIngreso.csv")

graficoTienda.graficoLinea("ropa", "price")
graficoIngresos.graficoDispersion("fuente", "ingresos")