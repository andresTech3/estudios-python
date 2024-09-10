from tkinter import *

root= Tk()
root.title("Curso de Tk")
entrada = Entry(root)
entrada.insert(0, "ingrese su nombre")

#* el metodo bind() permite capturar un evento y asociarle una llamada a una funcion
entrada.bind("<Button-1>", lambda x : entrada.delete(0, END)) #% establecer una tecla del mouse o teclado en este caso es el clik izquierdo del mouse

entrada.pack()

#* Evento para el boton
def btn():
    name = entrada.get() #% que obtenga el dato que le pasamos
    Label(root,text=name).pack()

#$ widget Botones
Button(root,text="Enviar", command= btn).pack()



root.mainloop()

#$ objetos en tkinter
#? .pack() -> que se pueda mostrar en la pantalla
#* Label -> crear un panel
#* Button -> crear un boton
#* Entry -> para crear una Entrada de datos