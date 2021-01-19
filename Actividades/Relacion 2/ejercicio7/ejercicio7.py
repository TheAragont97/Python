diccionario={}
clave=input("Ingresa el nombre: ")
valor=input("Ingresa el número de teléfono: ")
diccionario[clave]=valor
op=input("¿Quieres seguir añadiendo datos al diccionario? S/N ")
op=op.upper()
while op!="N":
    clave=input("Ingresa el nombre: ")
    if clave in diccionario:
        print("Error, ya existe ese nombre en el diccionario")
    else:
        valor=input("Ingresa el número de teléfono: ")
        diccionario[clave]=valor
        op=input("¿Quieres seguir añadiendo datos al diccionario? S/N ").upper()



