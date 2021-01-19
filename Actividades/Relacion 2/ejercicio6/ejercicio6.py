lista=[1,2,3,4,5,6,7,8,1,1,1]
cont=0
x=int(input("Ingrese un número: "))
for i in range(len(lista)):
    if lista[i] == x :
        cont=cont+1
print("El número ",x," aparece : ",cont," veces.")