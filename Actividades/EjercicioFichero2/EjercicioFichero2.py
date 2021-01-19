def tabla(num):
    f=open("tabla-"+ str(num) +".txt","r")
    print(f.read())
try:
    num=int(input("Meta un número del 1-10: "))
    while num<=0 or num>10:
        num=int(input("Error, Meta un número del 1-10: "))
    tabla(num)
except FileNotFoundError:
    print("Error")
except:
    print("Solo se admiten números")
