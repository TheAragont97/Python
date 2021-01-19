def tabla(num,linea):
    f=open("tabla-"+ str(num) +".txt","r")
    lista=f.readlines()
    print(lista[linea-1])
try:
    num=int(input("Meta un número del 1-10: "))
    linea=int(input("Linea de la tabla: "))
    while num<=0 or num>10 or linea <0 or linea>10:
        num=int(input("Error, Meta un número del 1-10: "))
        linea=int(input("Linea de la tabla: "))
    tabla(num,linea)
except FileNotFoundError:
    print("Error")
except:
    print("Solo se admiten números")

