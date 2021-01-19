from Calculadora import *
while True:
    try:
        n1=float(input("Ingresa el primer número:  "))
        n2=float(input("Ingresa el segundo número:  "))
        break
    except ValueError:
        print("Opss! Error, solo se admiten números, vuelva a intentarlo..")
inst=Calculadora(n1,n2)
print("El resultado de la suma de ambos números es: ",inst.suma())
print("El resultado de la resta de ambos números es: ",inst.resta())
print("El resultado de la multiplicación de ambos números es: ",inst.multi())
print("El resultado de la división de ambos números es: ",inst.division())
