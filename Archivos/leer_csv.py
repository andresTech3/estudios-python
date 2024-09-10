import csv

with open("Archivos\\texto.csv") as file :
    reader = csv.reader(file)
    for row in reader:
        #? string.join -> me genera una secuencia de un elemento iterable
        print(row) 