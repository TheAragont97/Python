from Circulo import *
while True:
    try:
        radio=float(input("Ingresa el radio del círculo:  "))
        break
    except ValueError:
        print("Opss!, Error, el valor tiene que ser un número")
inst=Circulo(radio)
if inst.comprobacion()==True:
    inst.set_radio(radio)
    print("Este es el área del círculo: ",inst.area())
    print("Este es el perímetro del círculo: ",inst.perimetro())
else:
    print("Vuelva a iniciar el programa")