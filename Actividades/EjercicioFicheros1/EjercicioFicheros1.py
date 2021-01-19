tablas = [];
def tabla(num):
    op=True
    tablas.sort
    for y in range(len(tablas)):
        if(y!=num):
            op=True
        else:
            op=False
    if(op):
        tablas.extend(str(num))
        f=open("tabla-"+ str(num) +".txt","w")
        for x in range(11):
            f.write(str(num)+" * "+str(x)+" = "+str(num*x)+"\n")
    else:
        print("Ya esta creada la tabla del "+num)


try:
    for x in range(10):
        num=int(input("Meta un número del 1-10: "))
        while num<=0 or num>10:
            num=int(input("Error, Meta un número del 1-10: "))
        tabla(num)
except FileNotFoundError:
    print("Error")
except:
    print("Solo se admiten números")