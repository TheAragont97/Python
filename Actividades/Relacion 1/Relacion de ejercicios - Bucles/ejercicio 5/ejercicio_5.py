cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
anos = int(input("¿Años?"))
for i in range(anos):
    cantidad *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))
