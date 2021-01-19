import mysql.connector
class Mostrar:
    def __init__(self):
        self.x=""
        self.lista=[]
        self.d={}
    def Consulta_Equipo(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from equipo"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[0]]=datos[1]
                self.lista.append(datos[0])
                print("ID: "+str(datos[0])+" nombre: "+str(datos[1]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Consulta_Partido(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from partidos"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[0]]=datos[2]
                self.lista.append(datos[0])
                print("ID: "+str(datos[0])+" fecha del partido: "+str(datos[2]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Consulta_Jugador(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from jugador"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[0]]=datos[2]
                self.lista.append(datos[0])
                print("ID: "+str(datos[0])+" nombre: "+str(datos[2]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Consulta_Presidente(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from presidente"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[0]]=datos[2]
                self.lista.append(datos[0])
                print("DNI: "+str(datos[0])+" nombre: "+str(datos[2]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Consulta_Gol(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from goles"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[0]]=datos[2]
                self.lista.append(datos[0])
                print("ID: "+str(datos[0])+" momento del gol: "+str(datos[2]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Consulta_Partido_Gol(self):
        try:
            self.lista=[]
            self.d={}
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
            #Consulta sql#
            sql="select * from partidos"
            #Para enviar la consulta#
            cursor.execute(sql)
            #Para recibir los resultados#
            resultados=cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.d[datos[1]]=datos[0]
                self.lista.append(datos[0])
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")