import mysql.connector
from Mostrar import *
class ConsultaColumna:
    def __init__(self):
        self.__m=Mostrar()
    def Menu_Consulta(self,num):
            while True:
                try:
                    print("------Elige el tipo de consulta------ \n 1.Consulta Simple (Sin Where) \n 2.Consulta Compleja (Con Where)")
                    x=int(input("Ingresa la opción: "))
                    while x<0 and x>2:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Elige el tipo de consulta------ \n 1.Consulta Simple (Sin Where) \n 2.Consulta Compleja (Con Where)")
                        x=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if x==1:
                self.Consulta_Simple(num)
            elif x==2:
                self.Consulta_Compleja(num)

    def Consulta_Simple(self,num):
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
            if num==1:
                #Consulta sql#
                sql="select * from jugador"
                #Para enviar la consulta#
                cursor.execute(sql)
                #Para recibir los resultados#
                resultados=cursor.fetchall()
                #Estos se imprimen#
                #print(resultados)#
                #Para mejorar el aspecto de los resultados#
                if resultados!=None and resultados!="":
                    for datos in resultados:
                        print(datos)
                else:
                    print("No se encontró nada")
                conexion.commit()
                cursor.close()
                conexion.close()
            elif num==2:
                #Consulta sql#
                sql="select * from equipo"
                #Para enviar la consulta#
                cursor.execute(sql)
                #Para recibir los resultados#
                resultados=cursor.fetchall()
                #Estos se imprimen#
                #print(resultados)#
                #Para mejorar el aspecto de los resultados#
                if resultados!=None and resultados!="":
                    for datos in resultados:
                        print(datos)
                else:
                    print("No se encontró nada")
                conexion.commit()
                cursor.close()
                conexion.close()
            elif num==3:
                #consulta sql#
                sql = "select * from presidente"
                #Para enviar la consulta#
                cursor.execute(sql)
                #Para recibir los resultados#
                resultados=cursor.fetchall()
                #Estos se imprimen#
                #print(resultados)#
                #Para mejorar el aspecto de los resultados#
                if resultados!=None and resultados!="":
                    for datos in resultados:
                        print(datos)
                else:
                    print("No se encontró nada")
                conexion.commit()
                cursor.close()
                conexion.close()
            elif num==4:
                #consulta sql#
                sql = "select * from goles"
                #Para enviar la consulta#
                cursor.execute(sql)
                #Para recibir los resultados#
                resultados=cursor.fetchall()
                #Estos se imprimen#
                #print(resultados)#
                #Para mejorar el aspecto de los resultados#
                if resultados!=None and resultados!="":
                    for datos in resultados:
                        print(datos)
                else:
                    print("No se encontró nada")
                conexion.commit()
                cursor.close()
                conexion.close()
            elif num==5:
                #consulta sql#
                sql = "select * from partidos"
                #Para enviar la consulta#
                cursor.execute(sql)
                #Para recibir los resultados#
                resultados=cursor.fetchall()
                #Estos se imprimen#
                #print(resultados)#
                #Para mejorar el aspecto de los resultados#
                if resultados!=None and resultados!="":
                    for datos in resultados:
                        print(datos)
                else:
                    print("No se encontró nada")
                conexion.commit()
                cursor.close()
                conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")


    def Consulta_Compleja(self,num):
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
            op_fallo=False
            if num==1:
                op=False
                #consulta sql#
                sql = "select * from jugador where cod_jugador = %s "
                while op!=True:
                    self.__m.Consulta_Jugador()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del jugador: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(j,))
                    #Guardamos el resutlado en la variable y la mostramos#
                    resultados =  cursor.fetchone()
                    print(resultados)
            if num==2:
                op=False
                #consulta sql#
                sql = "select * from equipo where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        k=int(input("Elige una id del equipo: "))
                        for i in self.__m.lista:
                            if int(i)==k:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(k,))
                    #Guardamos el resutlado en la variable y la mostramos#
                    resultados =  cursor.fetchone()
                    print(resultados)
            if num==3:
                op=False
                #consulta sql#
                sql = "select * from presidente where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        h=input("Elige un dni del presidente: ")
                        for i in self.__m.lista:
                            if i==h:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(h,))
                    #Guardamos el resutlado en la variable y la mostramos#
                    resultados =  cursor.fetchone()
                    print(resultados)
            if num==4:
                op=False
                #consulta sql#
                sql = "select * from goles where cod_gol = %s "
                while op!=True:
                    self.__m.Consulta_Gol()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        l=int(input("Elige una id del gol: "))
                        for i in self.__m.lista:
                            if int(i)==l:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(l,))
                    #Guardamos el resutlado en la variable y la mostramos#
                    resultados =  cursor.fetchone()
                    print(resultados)
            if num==5:
                op=False
                #consulta sql#
                sql = "select * from partidos where cod_partido = %s "
                while op!=True:
                    self.__m.Consulta_Partido()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        o=int(input("Elige una id del partido: "))
                        for i in self.__m.lista:
                            if int(i)==o:
                                op=True
                                break
                if op_fallo!=True:    
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(o,))
                    #Guardamos el resutlado en la variable y la mostramos#
                    resultados =  cursor.fetchone()
                    print(resultados)
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")