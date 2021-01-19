#creamos un método en el que vamos a ver cuantas filas de la pirámide se pueden hacer
def construccion(bloques):
	fila=0
	finaliza=False
	#hacemos un bucle para comprobar cuantas filas se pueden hacer y si se puede terminar la construcción
	while(bloques!=0):
		#si el bloque es mayor que la fila se puede construir y hacemos dentro los calculos necesarios
		if(bloques>=fila):
			finaliza=True
			fila+=1
			bloques-=fila
		#sino no se puede seguir construyendo y sale del bucle
		else:
			finaliza=False
			print("No se puede contruir la pirámide")
			break
	#si ha finalizado con exito o no, mostramos diferentes mensajes
	if(finaliza):
		print("Este es el número de filas que se pueden construir (finalizada): ",fila)
	else:
		print("Este es el número de filas en el que se han quedado los constructores (pirámide sin acabar): ",fila)
#validamos que el usuario solo pueda introducir números
try:
	bloques=int(input("Meta el número de bloques: "))
	construccion(bloques)
except:
	print("Error, solo se admiten números")
