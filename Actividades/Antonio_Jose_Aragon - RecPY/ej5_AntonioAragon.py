#creamos el método para comprobar si contienen el mismo número de numeros repetidos
def igualdad(num1,num2):
	#creamos 2 listas para meter los números en los bulces siguientes
	numero1=[]
	numero2=[]
	#metemos en las listas estos números
	for x in range(4):
		numero1.extend(str(num1)[x])
	for y in range(4):
		numero2.extend(str(num2)[y])
	#ordenamos las listas
	numero1.sort()
	numero2.sort()
	#comparamos si son iguales o no
	if(numero1==numero2):
		#si lo son, contienen los mismos números
		print("Contienen los mismos números")
	else:
		#sino, no contienen los mismo números
		print("No contienen los mismo números")
#validamos si se introduce o no números
try:
	#le pedimos 2 números al usuario, sino son correctos los vuelve a pedir hasta que lo sean
	num1=int(input("Meta el primer número: "))
	num2=int(input("Meta el segundo número: "))
	op=False
	#comprobamos si son mayores o iguales a 1000 y menores o iguales a 9999
	if(num1>=1000 and num1<=9999 and num2>=1000 and num2<=9999):
		op=True
	else:
		op=False
	#sino es correcto lo vuelve a pedir en el bucle hasta que sean correctos
	while op==False:
		print("Vuelva a introduccir los datos correctamente")
		num1=int(input("Meta el primer número: "))
		num2=int(input("Meta el segundo número: "))
		if(num1>=1000 and num1<=9999 and num2>=1000 and num2<=9999):
			op=True
		else:
			op=False
	#una vez sean correctos se lo pasamos al método
	igualdad(num1,num2)
except:
	print("Error, solo se admiten números")