from Gestion_Alumno import *
from Email import *
class Main:
    def __init__(self):
        self.__g=Gestion_Alumno()
        self.__e=Email()
    def Aula(self):
        while True:
            op=0
            while op<1 or op>3:
                try:
                    op=int(input("********** AULA PYTHON ************ \n 1.Gestión de alumnos. \n 2.Enviar correo. \n 3.Salir \n Elige una opción: "))
                except ValueError:
                    print("Error, no se admiten letras, solo números")
            if op==1:
                self.Gestion()
            elif op==2:
                self.Enviar()
            elif op==3:
                print("Gracias, Hasta luego")
                sys.exit(0)
    def Gestion(self):
        while True:
            op=0
            while op<1 or op>4:
                try:
                    op=int(input("******** GESTIÓN  DE ALUMNADO ******** \n 1.Añadir alumnos. \n 2.Modificar datos de alumnos \n 3.Eliminar alumnos \n 4.Volver al Menú Inicial \n Elige una opción: "))
                except ValueError:
                    print("Error, no se admiten letras, solo números")
            if op==1:
                self.__g.Anadir()
            elif op==2:
                self.__g.Modificar()
            elif op==3:
                self.__g.Eliminar()
            elif op==4:
                self.Aula()
    def Enviar(self):
        while True:
            op=0
            while op<1 or op>3:
                try:
                    op=int(input("********** ENVIAR CORREO ************ \n 1.Introducir datos del correo. \n 2.Enviar correo. \n 3.Volver al Menú Inicial \n Elige una opción: "))
                except ValueError:
                    print("Error, no se admiten letras, solo números")
            if op==1:
                self.__e.Introducir()
            elif op==2:
                self.__e.Enviar_Correo()
            elif op==3:
                self.Aula()