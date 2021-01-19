diccionario={'1234567890':'200'}
pagado=0
deuda=0
op=input("¿Desea añadir una factura, pagar una factura o terminar? A/P/T : ").upper()
if op=="A" or op=="P" or op=="T":
    while op!="T":
       if op=="A":
           factura=input("Ingrese el número de factura: ")
           coste=input("Ingrese el coste de la factura: ")
           diccionario[factura]=coste
       else:
           print(diccionario)
           pagar=input("¿Cual deseas pagar? :")
           pagado=diccionario[pagar]
           del diccionario[pagar]
           print("Se ha pagado: ",pagado)
           for i in diccionario.values():
                deuda=0
                deuda=deuda+int(i);
           print("Se tiene que pagar: ",deuda)
       op=input("¿Desea añadir una factura, pagar una factura o terminar? A/P/T : ").upper()
    print("Se ha pagado: ",pagado)
    for i in diccionario.values():
        deuda=0
        deuda=deuda+int(i);
    print("Se tiene que pagar: ",deuda)
else:
    print("Error")