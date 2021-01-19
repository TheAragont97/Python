nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")
if (sexo == "M" and nombre.lower() < 'm') or (sexo == "H" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es " + grupo)
