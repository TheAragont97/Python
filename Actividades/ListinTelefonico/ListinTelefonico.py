def menu():
    try:
        op=int(input("\nListín telefónico \n"+
             "============================ \n"+
             "1 - Consultar un teléfono \n"+
             "2 - Añadir un teléfono \n"+
             "3 - Eliminar un teléfono \n"+
             "4 - Crear el listín \n"+
             "0 - Terminar \n"))
        if(op==1):
            consulta()
        elif(op==2):
            anadir()
        elif(op==3):
            eliminar()
        elif(op==4):
            crear()
        elif(op==0):
            salir()
        else:
            print("Error, la opción introducida no es correcta")
    except:
         print("Error, solo se admiten números")
def consulta():
    numero=input("Introduzca el número de teléfono que quieres encontrar: ")
    encontrado=True
    if(len(numero)!=9):
        print("Error, vuelva a introducir el número")
        consulta()
    f=open("listin.txt",'r')
    for linea in f:
        if(str(linea).find(numero)!=-1):
            print("Lo encontré: "+str(linea).replace(',',':'))
            encontrado=True
            break
        else:
            encontrado=False
    if(encontrado==False):
        print("No existe el número de teléfono")
    f.close()
    menu()
def anadir():
    nombre=input("Introduzca el nombre que quieres añadir: ")
    numero=input("Introduzca el número de teléfono que quieres añadir: ")
    if(len(numero)!=9):
        print("Error, vuelva a introducir el número")
        anadir()
    f=open("listin.txt",'a')
    f.writelines(str(nombre)+","+str(numero)+"\n")
    f.close()
    print("Se ha añadido correctamente")
    menu()
def eliminar():
    numero=input("Introduzca el número de teléfono que quieres eliminar: ")
    if(len(numero)!=9):
        print("Error, vuelva a introducir el número")
        eliminar()
    f=open("listin.txt",'r')
    cadena=""
    for linea in f:
        if(str(linea).find(numero)==-1):
            cadena+=str(linea)+"\n"
    f.close()
    f=open("listin.txt",'w')
    f.write(cadena)
    f.close()
    print("Se ha eliminado correctamente")
    menu()
def crear():
    f=open("listin.txt",'a')
    print("Se ha creado el listin.txt")
    f.write("")
    f.close()
    menu()
def salir():
    print("Hasta luego")
    
print("Bienvenido")
menu()
    
