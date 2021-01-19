horas = float(input("Introduce las horas trabajadas: "))
coste = float(input("Introduce lo que cobras por hora trabajadas: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))
