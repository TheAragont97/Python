#Creamos un método para calcular el impuesto del ingreso del usuario
def calculadora(num):
	impuesto=0
	#en este if calculamos el impuesto siendo menor a 85528
	if(num<85528):
		impuesto=round((num*0.18)-556.2)
	#en este else calculamos el impuesto siendo mayor a 85528
	else:
		#calculamos el excente y si es menor a 0 decimos que es cero
		excedente=(num-85528)
		impuesto=round((excedente*0.32)+14839)
		if(impuesto<0):
			impuesto=0
	return impuesto
	#el impuesto lo pasamos redondeado como nos pide el ejercicio
#validamos que solo se meta un número flotante correctamente
try:
	#ingresa el número flotante el usuario
	ingreso=float(input("Ingrese el número: "))
	#mostramos el resultado por pantalla
	print(calculadora(ingreso))
except:
	print("Error, solo se admiten números")