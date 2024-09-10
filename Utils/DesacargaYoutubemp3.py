from pytube import YouTube
from tkinter import *
from tkinter import messagebox as messageBox

root = Tk();
root.config(bd=15)
root.title("Script Descargas")
imagen = PhotoImage(file='youtube_ico.png')
foto = Label(root, image= imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label = "para mas informacion", menu = helpmenu)
helpmenu.add_command(label = "informacion del autor", command=popup)