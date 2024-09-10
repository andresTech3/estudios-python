
#import mod_saludar as m_saludar
#import mod_saludar

#*acceder al modulo dentro de una carpeta en la misma ruta se importa asi
#from nom_carpeta.nom_modulo import *
#from nom_carpeta.nom_modulo import nombre_funcion
#*accerder al modulo dentro de una ruta distinta se importa asi
#? sys -> propiedades y funiones nativas de python
#? print(sys.builtin_module_names) -> tenemos todos los modulos nativos de python
import sys
print(sys.path.append('c:\Users\andres\OneDrive\Proyectos Web\Cursos de programacion\Python\Modulos\modulos.py'))

#! no es recomendable utilizar * para traer todos las funciones ya que sobrecarga con funciones que no vamos a utilizar
from mod_saludar import saludar,saludarRaro,educacion

#? as -> es para asignar en este caso modulos

print(saludar('deidy'))
print(saludarRaro('benny'))
print(educacion)

#* para ver las propiedades y metodos del namespace
print(dir(educacion))

#* haceder al nombre de este modulo 
print(__name__)

#* acedemos al nombre del modulo llamado
print(saludar.__name__)

