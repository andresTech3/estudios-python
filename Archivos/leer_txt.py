archive = open('archivos\\texto.txt') #habrimos el archivo-> (//) vamos a ir por una ruta


#*leemos el archivo completo
#¡print(archive.read()) 

#*leer una linea x linea
#¡print(archive.readlines())

#* leer una linea individualmente
print(archive.readline(100))

#*cerrar el archivo completo
archive.close()


