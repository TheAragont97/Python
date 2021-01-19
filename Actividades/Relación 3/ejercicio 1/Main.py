from ToRomano import *
while True:
    try:
        x=int(input("Ingresa un número para convertir a números romanos: "))
        break
    except ValueError:
        print("Oops! El valor introducido no era un número, intentelo de nuevo....")
inst=ToRomano(x)
inst.conversion(x)