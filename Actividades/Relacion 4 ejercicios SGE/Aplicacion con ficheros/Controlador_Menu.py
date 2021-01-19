from Comprobar_Alumno import *
from Comprobar_Notas import *
from POCO_Alumno import *
from POCO_Notas import *
class Controlador_Menu:
    def __init__(self):
        self.__comp_al=Comprobar_Alumno()
        self.__comp_no=Comprobar_Notas()
        self.__alumno=POCO_Alumno()
        self.__nota=POCO_Notas()
    def Insertar_Alumno(self):
        op="Y"
        while op=="Y":
            Dni=input("Inserte el dni del Alumno: ")
            while self.__comp_al.Comprobar_dni(Dni)!=True:
                Dni=input("Inserte el dni del Alumno: ")
            nom=input("Inserte el nombre del Alumno: ")
            while self.__comp_al.Comprobar_nombre(nom)!=True:
                nom=input("Inserte el nombre del Alumno: ")
            dir=input("Inserte la dirección del Alumno: ")
            while self.__comp_al.Comprobar_dir(dir)!=True:
                dir=input("Inserte la dirección del Alumno: ")
            while True:
                try:
                    edad=int(input("Inserte la edad del Alumno: "))
                    while self.__comp_al.Comprobar_edad(edad)!=True:
                        edad=int(input("Inserte la edad del Alumno: "))
                    break
                except ValueError:
                    print("Opss! Error, solo se admiten números, vuelva a intentarlo..")
            while True:
                try:
                    tlf=int(input("Inserte el teléfono del Alumno: "))
                    while self.__comp_al.Comprobar_tlf(tlf)!=True:
                        tlf=int(input("Inserte el teléfono del Alumno: "))
                    break
                except ValueError:
                    print("Opss! Error, solo se admiten números, vuelva a intentarlo..")
            beca=input("Inserte la beca del Alumno: ")
            while self.__comp_al.Comprobar_beca(beca)!=True:
                beca=input("Inserte la beca del Alumno: ")
            text_file=open("Alumnos.txt","a")
            text_file.write(Dni)
            text_file.write("\n")
            text_file.write(nom)
            text_file.write("\n")
            text_file.write(dir)
            text_file.write("\n")
            text_file.write(str(edad))
            text_file.write("\n")
            text_file.write(str(tlf))
            text_file.write("\n")
            text_file.write(beca.upper())
            text_file.write("\n")
            text_file.close()
            op=input("¿Desea seguir añadiendo datos de otro alumno? Y/N ").upper()
            while op!="Y" and op!="N":
                op=input("Error, la opción insertada es incorrecta, vuelva a intentarlo... ").upper()
    def Insertar_Notas(self):
        op="Y"
        while op=="Y":
            comp=False
            while comp==False:
                Dni=input("Inserte el dni del Alumno: ")
                while self.__comp_no.Comprobar_dni(Dni)!=True:
                    Dni=input("Inserte el dni del Alumno: ")
                fichero = open("Alumnos.txt","r")
                lineas = fichero.read()
                fichero.close()
                if lineas.find(Dni)!=-1:
                    comp=True
                else:
                    nuevo=input("El alumno no existe, ¿Desea introducir sus datos? Y/N ").upper()
                    while nuevo!="Y" and nuevo!="N":
                        nuevo=input("Opción incorrecta, vuelva a introducirla...").upper()
                    if nuevo=="Y":
                        self.Insertar_Alumno()
                        comp=True
                    else:
                        comp=False
            while True:
                    try:
                        notas1=int(input("Inserte la nota téorica del alumno: "))
                        while self.__comp_no.Comprobar_notas1(notas1)!=True:
                            notas1=int(input("Inserte la nota téorica del alumno: "))
                        break
                    except ValueError:
                        print("Opss! Error, solo se admiten números, vuelva a intentarlo..")
            while True:
                    try:
                        notas2=int(input("Inserte la nota prática del Alumno: "))
                        while self.__comp_no.Comprobar_notas2(notas2)!=True:
                            notas2=int(input("Inserte la nota prática del Alumno: "))
                        break
                    except ValueError:
                        print("Opss! Error, solo se admiten números, vuelva a intentarlo..")
            text_file=open("Notas.txt","a")
            text_file.write(Dni)
            text_file.write("\n")
            text_file.write(str(notas1))
            text_file.write("\n")
            text_file.write(str(notas2))
            text_file.write("\n")
            text_file.close()
            op=input("¿Desea seguir añadiendo notas de otro alumno? Y/N ").upper()
            while op!="Y" and op!="N":
                op=input("Error, la opción insertada es incorrecta, vuelva a intentarlo... ").upper()
    def Listar_beca(self):
        pos=[]
        lista_sin=[]
        fichero = open("Alumnos.txt","r")
        texto = fichero.readlines()
        fichero.close()
        for x in texto:
            lista_sin.append(x[:-1])
        cont=1
        for i in lista_sin:
            if i=="SI":
              pos.append(cont)
              cont=cont+1
            else:
              cont=cont+1
        print("Los Alumnos con Beca son: ")
        cont_pos=0
        for w in range(len(pos)):
            print(lista_sin[pos[cont_pos]-5])
            cont_pos=cont_pos+1
    def Buscar_alumno(self):
        pos_dni=0
        lista_sin=[]
        while True:
            try:
                Dni=input("Inserte el dni del alumno: ")
                while self.__comp_no.Comprobar_dni(Dni)!=True:
                    Dni=input("Inserte el dni del alumno: ")
                fichero = open("Notas.txt","r")
                texto = fichero.readlines()
                fichero.close()
                for x in texto:
                    lista_sin.append(x[:-1])
                cont=1
                pos_dni=lista_sin.index(Dni)
                print("DNI: ",lista_sin[pos_dni])
                print("Nota téorica: ",lista_sin[pos_dni+1])
                print("Nota práctica: ",lista_sin[pos_dni+2])
                break
            except ValueError:
                print("El dni no existe, intentelo de nuevo...")
    def Aprobados_general(self):
        fichero = open("Notas.txt","r")
        texto = fichero.readlines()
        fichero.close()
        dni=""
        pos1=1
        pos2=2
        nota1=0
        nota2=0
        lista_sin=[]
        lista_sin2=[]
        fichero2 = open("Alumnos.txt","r")
        texto2=fichero2.readlines()
        fichero2.close()
        for x in texto2:
            lista_sin2.append(x[:-1])
        for x in texto:
            lista_sin.append(x[:-1])
        for x in range(len(lista_sin)):
            if pos1<=len(lista_sin) and pos2<=len(lista_sin):
                notas1=int(lista_sin[pos1])
                notas2=int(lista_sin[pos2])
                if notas1>=5 and notas2>=5:
                   dni=lista_sin[pos1-1]
                   for i in lista_sin2:
                       if i==dni:
                           print(lista_sin2[lista_sin2.index(dni)+1]," ha sacado "
                                 ,notas1," en el téorico y un ",notas2," en el práctico")
                pos1=pos1+3
                pos2=pos2+3
    def Aprobado_teorica(self):
        fichero = open("Notas.txt","r")
        texto = fichero.readlines()
        fichero.close()
        dni=""
        pos1=1
        nota1=0
        lista_sin=[]
        lista_sin2=[]
        fichero2 = open("Alumnos.txt","r")
        texto2=fichero2.readlines()
        fichero2.close()
        for x in texto2:
            lista_sin2.append(x[:-1])
        for x in texto:
            lista_sin.append(x[:-1])
        for x in range(len(lista_sin)):
            if pos1<=len(lista_sin):
                notas1=int(lista_sin[pos1])
                if notas1>=5:
                   dni=lista_sin[pos1-1]
                   for i in lista_sin2:
                       if i==dni:
                           print(lista_sin2[lista_sin2.index(dni)+1]," ha sacado "
                                 ,notas1," en el téorico")
                pos1=pos1+3
    def Aprobado_practico(self):
        fichero = open("Notas.txt","r")
        texto = fichero.readlines()
        fichero.close()
        dni=""
        pos2=2
        nota2=0
        lista_sin=[]
        lista_sin2=[]
        fichero2 = open("Alumnos.txt","r")
        texto2=fichero2.readlines()
        fichero2.close()
        for x in texto2:
            lista_sin2.append(x[:-1])
        for x in texto:
            lista_sin.append(x[:-1])
        for x in range(len(lista_sin)):
            if pos2<=len(lista_sin):
                notas2=int(lista_sin[pos2])
                if notas2>=5:
                   dni=lista_sin[pos2-2]
                   for i in lista_sin2:
                       if i==dni:
                           print(lista_sin2[lista_sin2.index(dni)+1]," ha sacado "
                                 ,notas2," en el práctico")
                pos2=pos2+3
    def Menu(self):
        menu_op=False
        while menu_op==False:
            op=int(input("-------------Menú------------\n 1. Insertar datos personales del alumno/a.\n 2. Insertar calificaciones del alumno/a\n 3. Listar alumnado con beca.\n 4. Buscar calificaciones de un alumno/a.\n 5. Mostrar listado con nombre de alumnos/as que han aprobado la asignatura\n 6. Mostrar listado con nombre de alumnos/as que han aprobado solo la parte teórica.\n 7. Mostrar listado con nombre de alumnos/as que han aprobado sólo la parte práctica.\n 8. Salir.\n Elija una opción :"))
            if op<=0 and op>8:
                menu_op=False
                print("Error, la opción insertada no es correcta")
            else:
                if op==1:
                    self.Insertar_Alumno()
                    menu_op=False
                elif op==2:
                    self.Insertar_Notas()
                    menu_op=False
                elif op==3:
                    self.Listar_beca()
                    menu_op=False
                elif op==4:
                    self.Buscar_alumno()
                    menu_op=False
                elif op==5:
                    self.Aprobados_general()
                    menu_op=False
                elif op==6:
                    self.Aprobado_teorica()
                    menu_op=False
                elif op==7:
                    self.Aprobado_practico()
                    menu_op=False
                elif op==8:
                    print("Hasta luego")
                    menu_op=True