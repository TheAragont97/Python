#creamos un método para ver quitarle las vocales a la cadena y devolverlo en mayusculas
def devorador(cadena):
	cadenaCambiada=""
	#una vez creada la variable auxiliar para meter el resultado final
	#hacemos un bucle para ver si es vocal o no
	for y in cadena:
		#si no lo es entra en este if y mete las consonantes en mayuscula dentro de la variable nueva
		if(y!='a' and y!='e' and y!='i' and y!='o' and y!='u'):
			cadenaCambiada+=y.upper()
	#despues imprimimos el resultado
	print(cadenaCambiada)
#validamos si es correcto lo que el usuario a introducido
try:
	#hacemos que el usuario meta la cadena y se lo pasamos a la función
	cadena=input("Ingrese una cadena: ")
	devorador(cadena)
except:
	print("Error, no se han metido los valores correctos")
