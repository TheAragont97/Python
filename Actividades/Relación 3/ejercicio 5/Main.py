from Rectangulo import *
while True:
    try:
        base=float(input("Ingresa la base del rectángulo:  "))
        altura=float(input("Ingresa la altura del rectángulo: "))
        break
    except ValueError:
        print("Opss!, Error, el valor tiene que ser un número")
inst=Rectangulo(altura,base)
if inst.comprobacion()==True:
    inst.set_altura(altura)
    inst.set_base(base)
    print("Este es el área del rectángulo: ",inst.area())
else:
    print("Vuelva a iniciar el programa")