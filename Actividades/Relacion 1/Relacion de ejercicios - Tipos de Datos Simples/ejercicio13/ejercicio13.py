inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
ahorros_primero = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(ahorros_primero, 2)))
ahorros_segundo = ahorros_primero * (1 + interes)
print("Balance tras el segundo año:" + str(round(ahorros_segundo, 2)))
ahorros_tercero =ahorros_segundo * (1 + interes)
print("Balance tras el tercer año:" + str(round(ahorros_tercero, 2)))
