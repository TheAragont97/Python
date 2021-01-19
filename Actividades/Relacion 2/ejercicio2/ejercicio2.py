lista = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
x=int(input("Ingresa el número del mes que quieres que se muestre por pantalla: "))
if x>0 and x<13:
    print(lista[x-1])
else:
    print("Error, el valor introducido no es correcto")
