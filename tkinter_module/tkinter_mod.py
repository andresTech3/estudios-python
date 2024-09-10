from tkinter import *

#$ para representar una ventana principal
root = Tk() 

#*titulo de la ventana
root.title("curso de tkinder")

#*tamaño de la ventana + posicion de ubicacion (cordenadas de la pantalla)
root.geometry("800x600+250+50")

#*creacion de etiquetas
mensaje = Label(root,text="Mi primer programa con Tkinter").grid(row = 0,column = 0)
mensaje2 = Label(root,text="esta es la segunda etiqueta").grid(row = 0, column= 1)


#* mantener en loop la ventana
root.mainloop()

#$ temario de tkinter

#% title = titulo
#% label = etiqueta
#% root = raiz 
#% text = texto
#% pack = empaquetar
#% grid = cuadricula
#% mainloop = bucle principal
#% row = fila
#% column = columna






