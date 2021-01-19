diccionario={}
carac=input("Ingrese el dato nuevo para el diccionario: ")
dato=input("Ingrese el valor del dato: ")
diccionario[carac]=dato
print(diccionario)
op=input("¿Quiere seguir añadiendo datos? S/N :").upper()
if op=="S" or op=="N":
    while op=="S":
        carac=input("Ingrese el dato nuevo para el diccionario: ")
        dato=input("Ingrese el valor del dato: ")
        diccionario[carac]=dato
        print(diccionario)
        op=input("¿Quiere seguir añadiendo datos? S/N :").upper()
else:
    print("Opción incorrecta")

