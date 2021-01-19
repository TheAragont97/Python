import mysql.connector
from Mostrar import *
class Eliminar:
    def __init__(self):
        self.__m=Mostrar()
    def Jugador(self,x):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'liga'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            cursor = conexion.cursor()
            #consulta sql#
            op=False
            op_fallo=False
            if x==0:
                sql = "delete from jugador where cod_jugador = %s "
                while op!=True:
                    self.__m.Consulta_Jugador()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del jugador que quieres eliminar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(j,))
            else:
                sql = "delete from jugador where cod_equipo = %s "
                #Para ejecutar la consulta#
                cursor.execute(sql,(x,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Equipo(self):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'liga'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            cursor = conexion.cursor()
            #consulta sql#
            op=False
            op_fallo=False
            sql = "delete from equipo where cod_equipo = %s "
            while op!=True:
                self.__m.Consulta_Equipo()
                if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                else:
                    eq=int(input("Elige una id del equipo que quieres eliminar: "))
                    print("Con esto se eliminarán todos los datos enlazados al equipo que se quiere eliminar")
                    for i in self.__m.lista:
                        if self.__m.lista is not None or self.__m.lista is not []:
                            if int(i)==eq:
                                self.Jugador(eq)
                                self.Presidente(eq)
                                self.Partido(eq)
                                op=True
                                break
                    
            if op_fallo!=True:            
                #Para ejecutar la consulta#
                cursor.execute(sql,(eq,))
                #Guardamos el resutlado en la variable y la mostramos#
                resultados =  cursor.fetchone()
                conexion.commit()
                cursor.close()
                conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Presidente(self,x):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'liga'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            cursor = conexion.cursor()
            #consulta sql#
            op=False
            op_fallo=False
            if x==0:
                sql = "delete from presidente where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige un dni del presidente que quieres eliminar: ")
                        for i in self.__m.lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(j,))
            else:
                sql = "delete from presidente where cod_equipo = %s "
                #Para ejecutar la consulta#
                cursor.execute(sql,(x,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Gol(self,x):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'liga'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            cursor = conexion.cursor()
            #consulta sql#
            op=False
            op_fallo=False
            if x==0:
                sql = "delete from goles where cod_gol = %s "
                while op!=True:
                    self.__m.Consulta_Gol()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del gol que quieres eliminar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(j,))
            else:
                sql = "delete from goles where cod_partido = %s "
                #Para ejecutar la consulta#
                cursor.execute(sql,(x,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Partido(self,x):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'liga'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            cursor = conexion.cursor()
            #consulta sql#
            op=False
            op_fallo=False
            if x==0:
                sql = "delete from partidos where cod_partido = %s "
                while op!=True:
                    self.__m.Consulta_Partido()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del partido que quieres eliminar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                self.Gol(j)
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(j,))
            else:
                self.__m.Consulta_Partido_Gol()
                y=self.__m.d.get(x)
                self.Gol(y)
                sql = "delete from partidos where cod_equipo = %s "
                #Para ejecutar la consulta#
                cursor.execute(sql,(x,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")