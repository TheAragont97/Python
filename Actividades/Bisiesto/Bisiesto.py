#Atributos
listaAnnos = [1900, 2000, 2016, 1987]
listaMes = [2, 2, 1, 11]
def esBisiesto(anno):
    bisiesto=False
    if(anno%400==0):
        if(anno%100==0):
            if(anno%4==0):
                bisiesto=True
    if(bisiesto):
        print("tiene 29 dias el año "+str(anno))
    else:
        print("tiene 28 dias el año "+str(anno))
def diasEnMes(anno,mes):
    if(mes==1):
        print("Este mes "+str(mes)+" tiene 30 dias el año "+str(anno))
    elif(mes==11):
        print("Este mes "+str(mes)+" tiene 31 dias el año "+str(anno))
    else:
        print("Este mes "+str(mes)+"",end='\n')
        esBisiesto(anno);
for x in listaAnnos:
    for y in listaMes:
        diasEnMes(int(x),int(y))