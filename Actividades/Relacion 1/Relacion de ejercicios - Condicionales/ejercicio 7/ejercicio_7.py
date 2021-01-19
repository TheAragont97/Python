renta = float(input("¿Cuál es tu renta anual? "))
if renta < 10000:
    p = 5
elif renta < 20000:
    p = 15
elif renta < 35000:
    p = 20
elif renta < 60000:
    p = 30
else:
    p = 45
print("Tu tipo impositivo es " + str(p) + "%")
