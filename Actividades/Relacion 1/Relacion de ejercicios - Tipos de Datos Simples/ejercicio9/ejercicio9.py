peso = input("Ingrese su peso en Kg: ")
altura = input("Ingrese su altura en M: ")
indice = round(float(peso)/float(altura)**2,2)
print("Tu índice de masa corporal es " + str(indice))