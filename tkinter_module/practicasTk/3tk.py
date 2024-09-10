from tkinter import *
root = Tk()

#*geometry
root.geometry("800x600+250+50")

#* entrada de datos para nombre
Label(root,text="Nombre : ").grid(row=0, column=0)
inputNombre = Entry(root)
inputNombre.grid(row=0, column=1)

#* entrada de datos para edad
Label(root,text="Edad : ").grid(row=1, column=0)
inputEdad = Entry(root)
inputEdad.grid(row=1, column=1)

#* boton

def info():
    name = inputNombre.get()
    age = inputEdad.get()
    Label(root, text=f"mi nombre es {name} y tengo {age}").grid(row=3,column=1)

Button(root,text="Enviar", command=info).grid(row=2, column=1)






root.mainloop()
