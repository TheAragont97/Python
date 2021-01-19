import mysql.connector
from Mostrar import *
from datetime import *
class Update:
    def __init__(self):
        self.__m=Mostrar()
    def Jugador(self):
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
            op_nom=False
            op_f=False
            op_fallo=False
            while True:
                try:
                    print("------Actualizar Jugador------ \n 1.Nombre \n 2.Fecha de nacimiento \n 3.Posición")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>3:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Actualizar Jugador------ \n 1.Nombre \n 2.Fecha de nacimiento \n 3.Posición")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update jugador set nombre = %s where cod_jugador = %s "
                while op!=True:
                    self.__m.Consulta_Jugador()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del jugador que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner al jugador seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))

            elif y==2:
                sql = "update jugador set fecha_nac = %s where cod_jugador = %s "
                while op!=True:
                    self.__m.Consulta_Jugador()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del jugador que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_f!=True:
                        while True:
                            try:
                                ano=int(input("Ingresa el año de nacimiento del jugador: "))
                                mes=int(input("Ingresa el mes de nacimiento del jugador: "))
                                dia=int(input("Ingresa el día de nacimiento del jugador: "))
                                if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                    op_f=False
                                else:
                                    date = datetime(year=ano, month=mes, day=dia)
                                    op_f=True
                                    break
                            except ValueError:
                                print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(date,j,))
            elif y==3:
                sql = "update jugador set posicion = %s where cod_jugador = %s "
                while op!=True:
                    self.__m.Consulta_Jugador()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del jugador que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while True:
                        try:
                            print("------Posición del jugador------ \n 1.Portero \n 2.Defensa \n 3.Centrocampista \n 4.Delantero")
                            z=int(input("Ingresa la opción: "))
                            while y<0 and y>4:
                                print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                                print("------Posición del jugador------ \n 1.Portero \n 2.Defensa \n 3.Centrocampista \n 4.Delantero")
                                z=int(input("Ingresa la opción: "))
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    if z==1:
                        pos="Portero"
                    elif z==2:
                        pos="Defensa"
                    elif z==3:
                        pos="Centrocampista"
                    elif z==4:
                        pos="Delantero"
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(pos,j,))
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
            op_nom=False
            op_f=False
            op_aforo=False
            op_fallo=False
            while True:
                try:
                    print("------Actualizar Equipo------ \n 1.Nombre \n 2.Estadio \n 3.Aforo \n 4.Fundación \n 5.Ciudad")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>3:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Actualizar Equipo------ \n 1.Nombre \n 2.Estadio \n 3.Aforo \n 4.Fundación \n 5.Ciudad")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update equipo set nombre = %s where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del equipo que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:   
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner al equipo seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))

            elif y==2:
                sql = "update equipo set estadio = %s where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del equipo que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner al estadio del equipo seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))
            elif y==3:
                sql = "update equipo set aforo = %s where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del equipo que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while True:
                        try:
                            while op_aforo!=True:
                                aforo=int(input("Ingresa el aforo del estadio: "))
                                if aforo>-1:
                                    op_aforo=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(aforo,j,))
            elif y==4:
                sql = "update equipo set fundacion = %s where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del equipo que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_f!=True:
                        while True:
                            try:
                                ano=int(input("Ingresa el año de fundación del equipo: "))
                                mes=int(input("Ingresa el mes de fundación del equipo: "))
                                dia=int(input("Ingresa el día de fundación del equipo: "))
                                if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                    op_f=False
                                else:
                                    date = datetime(year=ano, month=mes, day=dia)
                                    op_f=True
                                    break
                            except ValueError:
                                print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(date,j,))
            elif y==5:
                sql = "update equipo set ciudad = %s where cod_equipo = %s "
                while op!=True:
                    self.__m.Consulta_Equipo()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del equipo que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner a la ciudad del equipo seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Presidente(self):
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
            op_nom=False
            op_f=False
            op_aforo=False
            op_fallo=False
            while True:
                try:
                    print("------Actualizar Presidente------ \n 1.Nombre \n 2.Apellidos \n 3.Fecha Nacimiento \n 4.Años de Presidente")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>3:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Actualizar Presidente------ \n 1.Nombre \n 2.Apellidos \n 3.Fecha Nacimiento \n 4.Años de Presidente")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update presidente set nombre = %s where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige un dni del presidente que quieres actualizar: ")
                        for i in self.__m.lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner al presidente seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))

            elif y==2:
                sql = "update presidente set apellidos = %s where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige un dni del presidente que quieres actualizar: ")
                        for i in self.__m.lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_nom!=True:
                        nom=input("¿Que apellidos le quieres poner al presidente seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))
            elif y==3:
                sql = "update presidente set fec_nacimiento = %s where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige un dni del presidente que quieres actualizar: ")
                        for i in self.__m.lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_f!=True:
                        while True:
                            try:
                                ano=int(input("Ingresa el año de nacimiento del presidente: "))
                                mes=int(input("Ingresa el mes de nacimiento del presidente: "))
                                dia=int(input("Ingresa el día de nacimiento del presidente: "))
                                if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                    op_f=False
                                else:
                                    date = datetime(year=ano, month=mes, day=dia)
                                    op_f=True
                                    break
                            except ValueError:
                                print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(date,j,))
            elif y==4:
                sql = "update presidente set ano_presidente = %s where dni = %s "
                while op!=True:
                    self.__m.Consulta_Presidente()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige un dni del presidente que quieres actualizar: ")
                        for i in self.__m.lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:
                    while op_f!=True:
                        while True:
                            try:
                                ano=int(input("Ingresa el año de presidente en el equipo: "))
                                mes=int(input("Ingresa el mes de presidente en el equipo: "))
                                dia=int(input("Ingresa el día de presidente en el equipo: "))
                                if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                    op_f=False
                                else:
                                    date = datetime(year=ano, month=mes, day=dia)
                                    op_f=True
                                    break
                            except ValueError:
                                print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(date,j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Gol(self):
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
            op_nom=False
            op_f=False
            op_aforo=False
            op_fallo=False
            while True:
                try:
                    print("------Actualizar Gol------ \n 1.Momento del gol \n 2.Descripción")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>2:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Actualizar Gol------ \n 1.Momento del gol \n 2.Descripción")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update goles set momento_gol = %s where cod_gol = %s "
                while op!=True:
                    self.__m.Consulta_Gol()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        k=int(input("Elige una id del gol que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==k:
                                op=True
                                break
                if op_fallo!=True:    
                    while True:
                        try:
                            while op_aforo!=True:
                                aforo=int(input("Ingresa el momento del gol: "))
                                if aforo>-1 and aforo<121:
                                    op_aforo=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(aforo,k,))

            elif y==2:
                sql = "update goles set descripcion = %s where cod_gol = %s "
                while op!=True:
                    self.__m.Consulta_Gol()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        k=int(input("Elige una id del gol que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==k:
                                op=True
                                break
                if op_fallo!=True:
                    while op_nom!=True:
                        nom=input("¿Que descripcion le quieres poner al presidente seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(nom,j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")

    def Partido(self):
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
            op_nom=False
            op_f=False
            op_aforo=False
            op_aforo2=False
            op_fallo=False
            while True:
                try:
                    print("------Actualizar Partido------ \n 1.Fecha del partido \n 2.Gol/es en casa \n 3.Gol/es fuera de casa")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>3:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Actualizar Partido------ \n 1.Fecha del partido \n 2.Gol/es en casa \n 3.Gol/es fuera de casa")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update partidos set fecha = %s where cod_partido = %s "
                while op!=True:
                    self.__m.Consulta_Partido()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del partido que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:    
                    while op_f!=True:
                        while True:
                            try:
                                ano=int(input("Ingresa el año en el que se jugó el partido: "))
                                mes=int(input("Ingresa el mes en el que se jugó el partido: "))
                                dia=int(input("Ingresa el día en el que se jugó el partido: "))
                                if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                    op_f=False
                                else:
                                    date = datetime(year=ano, month=mes, day=dia)
                                    op_f=True
                                    break
                            except ValueError:
                                print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(date,j,))

            elif y==2:
                sql = "update partidos set gol_casa = %s where cod_partido = %s "
                while op!=True:
                    self.__m.Consulta_Partido()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del partido que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True: 
                    while True:
                        try:
                            while op_aforo!=True:
                                aforo=int(input("Ingresa el gol anotado en casa: "))
                                if aforo>-1:
                                    op_aforo=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(aforo,j,))
            elif y==3:
                sql = "update partidos set gol_fuera = %s where cod_partido = %s "
                while op!=True:
                    self.__m.Consulta_Partido()
                    if not self.__m.lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige una id del partido que quieres actualizar: "))
                        for i in self.__m.lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True: 
                    while True:
                        try:
                            while op_aforo2!=True:
                                aforo2=int(input("Ingresa el gol anotado fuera de casa: "))
                                if aforo2>-1:
                                    op_aforo2=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    cursor.execute(sql,(aforo2,j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  cursor.fetchone()
            conexion.commit()
            cursor.close()
            conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")