nombres = ['andres', ' manuel', 'ana', ' maria', 'santiago', "maria"]
apellidos = ['narvaez', 'ozuna', ' puerta', 'baldasor', 'amante', "jaramillo"]

#* registrar esta informacion en un txt de forma optima

#? zip -> unifica los arreglos segun sus posiciones 
with open('Archivos_problema_resuelto\\nombres_y_apellido.txt', 'w') as file :
    file.writelines('los datos son :\n\n')
    #* optimizamos mucho mas el aareglo
    [file.writelines(f"Nombre : {n}\nApellidos : {a}\n -------- \n") for n,a in zip(nombres,apellidos)]


    # for n,a in zip(nombres, apellidos):
    #     file.writelines(f"Nombre : {n}\n Apellidos : {a}\n -------- \n")