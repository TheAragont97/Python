edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales? "))
if edad <= 16 or ingresos < 1000:
    print("No tienes que cotizar")
else:
    print("Tienes que cotizar")
