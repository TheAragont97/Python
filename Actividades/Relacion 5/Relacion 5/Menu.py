from Anadir import *
from Eliminar import *
from Mostrar import *
from Update import *
from ConsultaColumna import *
class Menu:
    def __init__(self):
        self.__a=Anadir()
        self.__m=Mostrar()
        self.__e=Eliminar()
        self.__u=Update()
        self.__c=ConsultaColumna()
    def Opcion_Menu(self):
        x=0
        while x!=5:
            while True:
                try:
                    print("------Menú------ \n 1.Inserción de datos \n 2.Eliminación de datos \n 3.Actualizar datos \n 4.Selección \n 5.Salir")
                    x=int(input("Ingresa la opción: "))
                    while x<0 and x>5:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Menú------ \n 1.Inserción de datos \n 2.Eliminación de datos \n 3.Actualizar datos \n 4.Selección \n 5.Salir")
                        x=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if x==1:
                self.Seleccion_Anadir()
            elif x==2:
                self.Seleccion_Eliminar()
            elif x==3:
                self.Seleccion_Update()
            elif x==4:
                self.Seleccion()
            elif x==5:
                print("Hasta luego")
    def Seleccion_Anadir(self):
        while True:
            try:
                print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                x=int(input("Ingresa la opción: "))
                while x<0 and x>5:
                    print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                    print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                    x=int(input("Ingresa la opción: "))
                break
            except ValueError:
                print("Error, solo se admiten números, intentelo de nuevo...")
        if x==1:
            self.__a.Jugador()
        elif x==2:
            self.__a.Equipo()
        elif x==3:
            self.__a.Presidente()
        elif x==4:
            self.__a.Gol()
        elif x==5:
            self.__a.Partido()
    def Seleccion_Eliminar(self):
        while True:
            try:
                print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                x=int(input("Ingresa la opción: "))
                while x<0 and x>5:
                    print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                    print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                    x=int(input("Ingresa la opción: "))
                break
            except ValueError:
                print("Error, solo se admiten números, intentelo de nuevo...")
        if x==1:
            self.__e.Jugador(0)
        elif x==2:
            self.__e.Equipo()
        elif x==3:
            self.__e.Presidente(0)
        elif x==4:
            self.__e.Gol(0)
        elif x==5:
            self.__e.Partido(0)
    def Seleccion_Update(self):
        while True:
            try:
                print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                x=int(input("Ingresa la opción: "))
                while x<0 and x>5:
                    print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                    print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                    x=int(input("Ingresa la opción: "))
                break
            except ValueError:
                print("Error, solo se admiten números, intentelo de nuevo...")
        if x==1:
            self.__u.Jugador()
        elif x==2:
            self.__u.Equipo()
        elif x==3:
            self.__u.Presidente()
        elif x==4:
            self.__u.Gol()
        elif x==5:
            self.__u.Partido()

    def Seleccion(self):
        w=0
        while w!=5:
            while True:
                try:
                    print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                    x=int(input("Ingresa la opción: "))
                    while x<0 and x>5:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Elige una tabla------ \n 1.Jugador \n 2.Equipo \n 3.Presidente \n 4.Goles \n 5.Partidos")
                        x=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if x==1:
                self.__c.Menu_Consulta(1)
            elif x==2:
                self.__c.Menu_Consulta(2)
            elif x==3:
                self.__c.Menu_Consulta(3)
            elif x==4:
                self.__c.Menu_Consulta(4)
            elif x==5:
                self.__c.Menu_Consulta(5)
            w=w+1