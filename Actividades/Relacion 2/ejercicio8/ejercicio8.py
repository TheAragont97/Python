diccionario={"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruta=input("Ingrese la fruta que quiere: ")
kilo=float(input("Ingrese el número de kilos que quiere de dicha fruta: "))
if fruta in diccionario:
    valor=diccionario.get(fruta)
    calculo=valor*kilo
    print("Te cuesta ",calculo," los ",kilo," kilos de ",fruta)
else:
    print("No existe esta fruta")

