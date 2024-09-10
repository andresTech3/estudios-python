from tkinter import *
root = Tk()


def actionBtn(indexBtn):
    etiqueta = Label(root,text=f"Boton {indexBtn} pulsado")
    etiqueta.pack()

btn1 = Button(root,text="btn1", command= lambda : actionBtn(1)).pack()
btn2 = Button(root,text="btn2", command= lambda : actionBtn(2)).pack()
btn3 = Button(root,text="btn3", command= lambda : actionBtn(3)).pack()
btn4 = Button(root,text="btn4", command= lambda : actionBtn(4)).pack()



root.mainloop()