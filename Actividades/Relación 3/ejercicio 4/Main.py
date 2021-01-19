from Palabra import *
while True:
    try:
        x=input("Ingresa una cadena: ")
        break
    except ValueError:
        print("Oops! El valor introducido no era válido, intentelo de nuevo....")
inst=Palabra(x)
inst.print_string()