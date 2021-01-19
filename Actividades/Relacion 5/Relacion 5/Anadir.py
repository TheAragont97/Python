import mysql.connector
from datetime import *
from Mostrar import *
class Anadir:
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
            op_nom=False
            op_f=False
            op_eq=False
            op_fallo=False
            nom_j=""
            date="1970-01-01"
            pos=""
            sqlInsertar = "insert INTO jugador(cod_jugador,cod_equipo,nombre,fecha_nac,posicion)values(%s,%s,%s,%s,%s)"
            #Insertamos esos parametros %s#
            while op_eq!=True:
                self.__m.Consulta_Equipo()
                if not self.__m.lista:
                    print("Esta vacío, por favor cree primero un equipo para enlazar a este jugador")
                    op_eq=True
                    op_fallo=True
                    break
                else:
                    eq=int(input("Elige una id del equipo: "))
                    for i in self.__m.lista:
                        if int(i)==eq:
                            op_eq=True
                            break
            if op_fallo!=True:
                while op_nom!=True:
                    nom_j=input("Ingresa el nombre del jugador: ")
                    if nom_j.isnumeric()==False and nom_j!="":
                        op_nom=True
                    else:
                        print("Error, el nombre no puede contener números o estar vacío")
                        op_nom=False
                while op_f!=True:
                    while True:
                        try:
                            ano=int(input("Ingresa el año de nacimiento del jugador: "))
                            mes=int(input("Ingresa el mes de nacimiento del jugador: "))
                            dia=int(input("Ingresa el día de nacimiento del jugador: "))
                            if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                print("No puede haber nacido antes del 1970 o después del 2002")
                                print("Los meses son del 1 al 12")
                                print("Los dias son desde el 1 al 31")
                                op_f=False
                            else:
                                date = datetime(year=ano, month=mes, day=dia)
                                op_f=True
                                break
                        except ValueError:
                            print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                    while True:
                        try:
                            print("------Posición del jugador------ \n 1.Portero \n 2.Defensa \n 3.Centrocampista \n 4.Delantero")
                            y=int(input("Ingresa la opción: "))
                            while y<0 and y>4:
                                print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                                print("------Posición del jugador------ \n 1.Portero \n 2.Defensa \n 3.Centrocampista \n 4.Delantero")
                                y=int(input("Ingresa la opción: "))
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    if y==1:
                        pos="Portero"
                    elif y==2:
                        pos="Defensa"
                    elif y==3:
                        pos="Centrocampista"
                    elif y==4:
                        pos="Delantero"
                    cursor.execute(sqlInsertar,('null',eq,nom_j,date,pos))
                    #Obligar a que se guarde de la cache#
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
            op_nom=False
            op_ciu=False
            op_est=False
            op_aforo=False
            op_f=False
            sqlInsertar = "insert INTO equipo(cod_equipo,nombre,estadio,aforo,fundacion,ciudad)values(%s,%s,%s,%s,%s,%s)"
            #Insertamos esos parametros %s#
            while op_nom!=True:
                nom_eq=input("Ingresa el nombre del equipo: ")
                if nom_eq.isnumeric()==False and nom_eq!="":
                    op_nom=True
                else:
                    print("Error, el nombre no puede contener números o estar vacío")
                    op_nom=False
            while op_ciu!=True:
                ciudad=input("Ingresa el nombre de la ciudad del equipo: ")
                if ciudad.isnumeric()==False and ciudad!="":
                     op_ciu=True
                else:
                    print("Error, el nombre no puede contener números o estar vacío")
                    op_ciu=False
            while op_est!=True:
                estadio=input("Ingresa el nombre del estadio: ")
                if estadio.isnumeric()==False and estadio!="":
                     op_est=True
                else:
                    print("Error, el nombre no puede contener números o estar vacío")
                    op_est=False
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
            while op_f!=True:
                while True:
                    try:
                        ano=int(input("Ingresa el año de fundación: "))
                        mes=int(input("Ingresa el mes de fundación: "))
                        dia=int(input("Ingresa el día de fundación: "))
                        if ano<1800 and mes<1 and mes>12 and dia<1 and dia>31:
                            print("No puede haberse antes del 1800")
                            print("Los meses son del 1 al 12")
                            print("Los dias son desde el 1 al 31")
                            op_f=False
                        else:
                            date = datetime(year=ano, month=mes, day=dia)
                            op_f=True
                            break
                    except ValueError:
                        print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
            cursor.execute(sqlInsertar,('null',nom_eq,estadio,aforo,date,ciudad))
            #Obligar a que se guarde de la cache#
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
            op_dni=False
            op_fallo=False
            op_eq=False
            op_nom=False
            op_ap=False
            op_f=False
            op_ano=False
            op_nom_eq=False
            op_f2=False
            ano=0
            sqlInsertar = "insert INTO presidente(dni,cod_equipo,nombre,apellidos,fec_nacimiento,ano_presidente,nom_equipo)values(%s,%s,%s,%s,%s,%s,%s)"
            #Insertamos esos parametros %s#
            
            while op_eq!=True:
                self.__m.Consulta_Equipo()
                if not self.__m.lista:
                    print("Esta vacío, por favor cree primero un equipo para enlazar a este presidente")
                    op_eq=True
                    op_fallo=True
                    break
                else:
                    eq=int(input("Elige una id del equipo: "))
                    for i in self.__m.lista:
                        if int(i)==eq:
                            nom_eq=self.__m.d.get(eq)
                            op_eq=True
                            break
            if op_fallo!=True:
                while op_dni!=True:
                    dni=input("Ingresa el DNI del presidente: ")
                    if len(dni)==9:
                        if dni[:-1].isnumeric()==True:
                            if dni[-1:].isnumeric()==True:
                                print("Error, El último dígito tiene que ser una letra")
                            else:
                                dni=dni.upper()
                                op_dni= True
                        else:
                            print("Error, Los ocho primeros dígitos tienen que ser números")
                    else:
                        print("Error, tiene que tener 9 carácteres")
                while op_nom!=True:
                    nom=input("Ingresa el nombre del presidente: ")
                    if nom.isnumeric()==False and nom!="":
                        op_nom=True
                    else:
                        print("Error, el nombre no puede contener números o estar vacío")
                while op_ap!=True:
                    ap=input("Ingresa los apellidos del presidente: ")
                    if ap.isnumeric()==False and ap!="":
                        op_ap=True
                    else:
                        print("Error, el nombre no puede contener números o estar vacío")
                while op_f!=True:
                    while True:
                        try:
                            ano=int(input("Ingresa el año de nacimiento del presidente: "))
                            mes=int(input("Ingresa el mes de nacimiento del presidente: "))
                            dia=int(input("Ingresa el día de nacimiento del presidente: "))
                            if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                print("No puede haber nacido antes del 1970 o después del 2002")
                                print("Los meses son del 1 al 12")
                                print("Los dias son desde el 1 al 31")
                                op_f=False
                            else:
                                date = datetime(year=ano, month=mes, day=dia)
                                op_f=True
                                break
                        except ValueError:
                            print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                while op_f2!=True:
                    while True:
                        try:
                            ano2=int(input("Ingresa el año en el que ingresó en el equipo el presidente: "))
                            mes2=int(input("Ingresa el mes en el que ingresó en el equipo el presidente: "))
                            dia2=int(input("Ingresa el día en el que ingresó en el equipo el presidente: "))
                            if ano2<1800 and ano2>2020 and mes2<1 and mes2>12 and dia2<1 and dia2>31 and ano2>(ano+17):
                                print("Solo puede ingresar con 18 años o más")
                                print("No puede haber ingresado antes del 1800 o después del 2020")
                                print("Los meses son del 1 al 12")
                                print("Los dias son desde el 1 al 31")
                                op_f2=False
                            else:
                                date2 = datetime(year=ano2, month=mes2, day=dia2)
                                op_f2=True
                                break
                        except ValueError:
                            print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                cursor.execute(sqlInsertar,(dni,eq,nom,ap,date,date2,nom_eq))
                #Obligar a que se guarde de la cache#
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
            op_min=False
            op_des=False
            op_part=False
            op_fallo=False
            sqlInsertar = "insert INTO goles(cod_gol,cod_partido,momento_gol,descripcion)values(%s,%s,%s,%s)"
            
            while op_part!=True:
                self.__m.Consulta_Partido()
                if not self.__m.lista:
                    print("Esta vacío, por favor cree primero un partido para enlazar a este gol")
                    op_part=True
                    op_fallo=True
                    break
                else:
                    part=int(input("Elige una id del partido: "))
                    for i in self.__m.lista:
                        if int(i)==part:
                            op_part=True
                            break
            if op_fallo!=True:
                while True:
                    try:
                        while op_min!=True:
                            min=int(input("Ingresa el minuto del gol: "))
                            if min>-1 and min<121:
                                op_min=True
                            else:
                                print("Error, el valor introduccido se pasa del tiempo de juego (partido + prórroga), intentelo de nuevo...")
                        break
                    except ValueError:
                        print("Error, solo se admiten números, intentelo de nuevo...")
                while op_des!=True:
                    des=input("Ingresa la descripción del gol: ")
                    if des.isnumeric()==False and des!="":
                        op_des=True
                    else:
                        print("Error, el nombre no puede contener números o estar vacío")
                #Insertamos esos parametros %s#
                cursor.execute(sqlInsertar,('null',part,min,des))
                #Obligar a que se guarde de la cache#
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
            op_eq=False
            op_f=False
            op_gc=False
            op_gf=False
            op_fallo=False
            sqlInsertar = "insert INTO partidos(cod_partido,cod_equipo,fecha,gol_casa,gol_fuera)values(%s,%s,%s,%s,%s)"
            #Insertamos esos parametros %s#
            while op_eq!=True:
                self.__m.Consulta_Equipo()
                if not self.__m.lista:
                    print("Esta vacío, por favor cree primero un equipo para enlazar a este partido")
                    op_eq=True
                    op_fallo=True
                    break
                else:
                    eq=int(input("Elige una id del equipo: "))
                    for i in self.__m.lista:
                        if int(i)==eq:
                            op_eq=True
                            break
            if op_fallo!=True:
                while op_f!=True:
                    while True:
                        try:
                            ano=int(input("Ingresa el año que se jugó el partido: "))
                            mes=int(input("Ingresa el mes que se jugó el partido: "))
                            dia=int(input("Ingresa el día que se jugó el partido: "))
                            if ano<1970 and ano>2002 and mes<1 and mes>12 and dia<1 and dia>31:
                                print("No puede haber nacido antes del 1970 o después del 2002")
                                print("Los meses son del 1 al 12")
                                print("Los dias son desde el 1 al 31")
                                op_f=False
                            else:
                                date = datetime(year=ano, month=mes, day=dia)
                                op_f=True
                                break
                        except ValueError:
                            print("Error, solo se admiten números y la fecha tiene que ser correcta, intentelo de nuevo...")
                while True:
                        try:
                            while op_gc!=True:
                                gc=int(input("Ingresa los goles en casa anotados: "))
                                if gc>-1 and gc<21:
                                    op_gc=True
                                else:
                                    print("Error, el valor introduccido se pasa del límite de 20 goles máximo, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                while True:
                        try:
                            while op_gf!=True:
                                gf=int(input("Ingresa los goles fuera de casa anotados: "))
                                if gf>-1 and gf<21:
                                    op_gf=True
                                else:
                                    print("Error, el valor introduccido se pasa del límite de 20 goles máximo, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                cursor.execute(sqlInsertar,('null',eq,date,gc,gf))
                #Obligar a que se guarde de la cache#
                conexion.commit()
                cursor.close()
                conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")