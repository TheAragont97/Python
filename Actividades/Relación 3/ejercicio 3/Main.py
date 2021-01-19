from POW import *
while True:
    try:
        base=int(input("Ingresa la base: "))
        exp=int(input("Ingresa el exponente: "))
        break
    except ValueError:
        print("Oops! El valor introducido no era válido, intentelo de nuevo....")
inst=POW(base,exp)
inst.calculo(base,exp)
