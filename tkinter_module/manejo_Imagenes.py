from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

#$ cargar la raiz principal
routerBase = os.path.dirname(__file__) 
#$ cargar las imagenes
file_images = os.path.join(routerBase,"img")
file_paisajes = os.path.join(file_images,"paisajes")
#* Bucle Ventana //////////////////////////////////////
root = Tk()
root.title("My App")
#% icono de ventana 
root.iconbitmap(os.path.join(file_images, "favicon.ico"))

#% carga de imagenes 
naturaleza = ImageTk.PhotoImage(Image.open(os.path.join(file_paisajes, "img1.jpg")).resize((350,200)))
layout = Label(image=naturaleza)
layout.pack()


root.mainloop()