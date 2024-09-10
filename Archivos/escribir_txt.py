with open("Archivos\\texto.txt","w",encoding="UTF-8") as file:
    #*sobrescribiendo el archivo
    #¡file.write("jajaja se mamo")
    #*nos pide una lista con toda las lineas y se va acomulando y no sobrescribe
    file.writelines(["hola como anda todo\n","misericordia"])