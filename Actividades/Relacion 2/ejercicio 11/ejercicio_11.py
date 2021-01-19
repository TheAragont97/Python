diccionario={}
op=1
while op!=6:
    print("------------Menú------------")
    print("1.Añadir Cliente")
    print("2.Eliminar Cliente")
    print("3.Mostrar Cliente")
    print("4.Listar todos los clientes")
    print("5.Listar clientes preferentes")
    print("6.Terminar")
    op=int(input("¿Que opción desea elegir? : "))
    if op<7 and op>0:
       if op==1:
            dic={}
            nif=input("Ingrese su NIF: ")
            #Se añade al sub-diccionario los datos#
            nombre=input("Ingrese su nombre: ")
            dic['Nombre']=nombre
            direccion=input("Ingrese su dirección: ")
            dic['Direccion']=direccion
            tlf=int(input("Ingrese su teléfono: "))
            dic['Telefono']=tlf
            correo=input("Ingrese su correo: ")
            dic['Correo']=correo
            preferente=input("Indique si es preferente o no (True/False): ")
            if preferente!= "True" or preferente!= "False":
                dic['Preferente']="False"
            else:
                dic['Preferente']=preferente
            #Se añade al diccionario la clave y el sub-diccionario#
            diccionario[nif]=dic
       elif op==2:
            print(diccionario.keys())
            borrar=input("¿Cual quiere eliminar?: ")
            del diccionario[borrar]
       elif op==3:
            print(diccionario.keys())
            mostrar=input("¿Cual quiere mostrar?: ")
            print(diccionario[mostrar])
       elif op==4:
            print(diccionario)
       elif op==5:
            for i in diccionario.values():
                if i.get("Preferente")=="True":
                    print("Datos: ",i)
    else:
       print("Error, opción incorrecta")
print("Hasta luego")