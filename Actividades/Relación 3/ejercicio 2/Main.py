from ToNumber import *
while True:
    try:
        x=input("Ingresa un número romano para convertir a números: ").upper()
        break
    except ValueError:
        print("Oops! El valor introducido no era válido, intentelo de nuevo....")
inst=ToNumber(x)
inst.conversion(x)
  
