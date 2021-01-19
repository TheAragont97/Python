from Triangulo import *
while True:
    try:
        lado1=float(input("Ingresa el primer lado del triángulo:  "))
        lado2=float(input("Ingresa el segundo lado del triángulo:  "))
        lado3=float(input("Ingresa el tercer lado del triángulo:  "))
        break
    except ValueError:
        print("Opss!, Error, el valor tiene que ser un número")
inst=Triangulo(lado1,lado2,lado3)
if inst.comprobacion()==True:
    inst.set_lado1(lado1)
    inst.set_lado2(lado2)
    inst.set_lado3(lado3)
    inst.lado_mayor()
    inst.tipo()
else:
    print("Vuelva a iniciar el programa")