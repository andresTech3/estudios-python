#* actua en consecuencia algun error

def suma():
    try:
        a = int(input("numero 1 :"))
        b = int(input("numero 2 :"))
        result = a + b
        
    except : 
        print("porfavor , no te detengas")
        suma()
    return result

print(suma())