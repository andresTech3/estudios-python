frase = input("desirme una frase y te digo cuanto tardaria en decirmelo: ")
palabras_separadas = frase.split(" ");
cantidad_palabras = len(palabras_separadas);
print(f"Dijiste {cantidad_palabras} palabras, y tardaste {cantidad_palabras / 2} segundo en decirlo")