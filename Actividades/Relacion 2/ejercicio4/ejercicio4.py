lista=[]
x=-1
while x!=0:
    x=int(input("Ingresa el número que quieres meter en la lista: "))
    if x!=0:
        lista.append(x)
    else:
        break
#Lista de menor a mayor#
lista_min=sorted(lista)
print("Lista de menor a mayor")
print("----------------------")
print(lista_min)
#Lista de mayor a menor#
lista_max=sorted(lista, reverse = True)
print("Lista de mayor a menor")
print("----------------------")
print(lista_max)

