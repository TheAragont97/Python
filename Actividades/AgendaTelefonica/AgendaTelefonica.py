key=""
value=""
nombre=""
diccionario={}
for x in range(1,5):
    print("Mete el nombre: ",end="")
    key=input()
    print("Mete el número de telefono: ",end="")
    value=int(input())
    diccionario[key]=value
print("De quien quieres saber el teléfono: ",end="")
nombre=input()
for d in diccionario:
    try:
        print("El teléfono de "+nombre+" es "+str(d[nombre]))
    except:
        print("No encuentro a "+nombre+" en mi agenda")

