#Creamos un metodo para ver si el año introducido es bisiesto o no
def bisiesto(anno):
	#Primero miramos si esta dentro del calendario gregoriano
	if(anno>=1582):
		#Si es así, miramos si es divisibel entre 4 para ver si es bisiesto o comun
		if(anno%4!=0):
			print("año común")
		#despues miramos si es divisible entre 100 para ver si es bisiesto o comun
		elif(anno%100!=0):
			print("año bisiesto")
		#despues miramos si es divisible entre 400 para ver si es bisiesto o comun
		elif(anno%400!=0):
			print("año común")
		#si es divisible entre todo lo anterior es bisiesto
		else:
			print("año bisiesto")
	#si no esta dentro del calendario gregoriano lo mostramos por pantalla
	else:
		print("No esta dentro del calendario gregoriano")
#valimos si es un número o no
try:
	#hacemos que el usuario ingrese el año
	anno=int(input("Meta el año para ver si es bisiesto o no: "))
	bisiesto(anno)
#sino es un número salta la excepción
except:
	print("Error, solo se admiten números")