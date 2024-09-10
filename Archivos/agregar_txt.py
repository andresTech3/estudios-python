with open("Archivos\\texto.txt","a",encoding="UTF-8") as file:
    #* agrega lineas a nuestro archivo
    #¡file.write("holaa mi bro todo bien")
    #*usando bucle for para agregar lineas
    file.write("\n")
    for i in range(5):
        file.write(f"linea {i} agregada \n")