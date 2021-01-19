import re, mysql.connector
class Gestion_Alumno:
    def __init__(self):
        self.__d={}
        self.__lista=[]
        self.cursor=""
        self.conexion=""
    def Conexion_BD(self):
        try:
            #diccionario que tiene las variables para conectar con la base de datos local#
            dbConnect = {
                'host':'localhost',
                'user':'root',
                'password':'',
                'database':'alumnado'
                }
            #Lo conectamos de esta manera, conexion establece la conexión#
            self.conexion = mysql.connector.connect(**dbConnect)
            #Nos permite enviar comandos al server y recibir los resultados#
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Anadir(self):
        try:
            self.Conexion_BD()
            #consulta sql#
            op_nom=False
            op_dir=False
            op_dni=False
            op_edad=False
            op_tlf=False
            op_correo=False
            sqlInsertar = "insert INTO alumnos(dni,nombre,direccion,edad,telefono,correo)values(%s,%s,%s,%s,%s,%s)"
            #Insertamos esos parametros %s#
            while op_dni!=True:
                    dni=input("Ingresa el DNI del alumno: ")
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
                nom=input("Ingresa el nombre del alumno: ")
                if nom.isnumeric()==False and nom!="":
                    op_nom=True
                else:
                    print("Error, el nombre no puede contener números o estar vacío")
                    op_nom=False
            while op_dir!=True:
                dir=input("Ingresa la dirección del alumno: ")
                if dir.isnumeric()==False and dir!="":
                    op_dir=True
                else:
                    print("Error, la dirección no puede contener números o estar vacío")
                    op_dir=False
            while True:
                    try:
                        while op_edad!=True:
                            edad=int(input("Ingresa la edad del alumno: "))
                            if edad>-1 and edad<100:
                                op_edad=True
                            else:
                                print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                        break
                    except ValueError:
                        print("Error, solo se admiten números, intentelo de nuevo...")
            while True:
                    try:
                        while op_tlf!=True:
                            tlf=int(input("Ingresa el teléfono del alumno: "))
                            if len(str(tlf))==9:
                                op_tlf=True
                            else:
                                print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                        break
                    except ValueError:
                        print("Error, solo se admiten números, intentelo de nuevo...")
            while op_correo!=True:
                correo=input("Ingresa el correo electrónico del alumno: ")
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
                    op_correo=True
                else:
                    print("Error, el correo introduccido no es correcto")
            self.cursor.execute(sqlInsertar,(dni,nom,dir,edad,tlf,correo))
            #Obligar a que se guarde de la cache#
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Buscar(self):
        try:
            self.Conexion_BD()
            #Consulta sql#
            sql="select * from alumnos"
            #Para enviar la consulta#
            self.cursor.execute(sql)
            #Para recibir los resultados#
            resultados=self.cursor.fetchall()
            #Estos se imprimen#
            #print(resultados)#
            #Para mejorar el aspecto de los resultados#
            for datos in resultados:
                self.__d[datos[0]]=datos[1]
                self.__lista.append(datos[0])
                print("DNI: "+str(datos[0])+" nombre: "+str(datos[1]))
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Modificar(self):
        try:
            self.Conexion_BD()
            #consulta sql#
            op=False
            op_nom=False
            op_edad=False
            op_tlf=False
            op_correo=False
            op_fallo=False
            while True:
                try:
                    print("------Modificar Alumno------ \n 1.Nombre \n 2.Dirección \n 3.Edad \n 4.Teléfono \n 5.Correo Electrónico")
                    y=int(input("Ingresa la opción: "))
                    while y<0 and y>5:
                        print("Error, la opción indicada es incorrecta, prueba de nuevo...")
                        print("------Modificar Alumno------ \n 1.Nombre \n 2.Dirección \n 3.Edad \n 4.Teléfono \n 5.Correo Electrónico")
                        y=int(input("Ingresa la opción: "))
                    break
                except ValueError:
                    print("Error, solo se admiten números, intentelo de nuevo...")
            if y==1:
                sql = "update alumnos set nombre = %s where dni = %s "
                while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige el dni del alumno que quieres actualizar: ")
                        for i in self.__lista:
                            if i==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while op_nom!=True:
                        nom=input("¿Que nombre le quieres poner al alumno seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, el nombre no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    self.cursor.execute(sql,(nom,j,))

            elif y==2:
                sql = "update alumnos set direccion = %s where dni = %s "
                while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige el dni del alumno que quieres actualizar: "))
                        for i in self.__lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while op_nom!=True:
                        nom=input("¿Que dirección le quieres poner al alumno seleccionado?: ")
                        if nom.isnumeric()==False and nom!="":
                            op_nom=True
                        else:
                            print("Error, la dirección no puede contener números o estar vacío")
                    #Para ejecutar la consulta#
                    self.cursor.execute(sql,(nom,j,))
            elif y==3:
                sql = "update alumnos set edad = %s where dni = %s "
                while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige el dni del alumno que quieres actualizar: "))
                        for i in self.__lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while True:
                        try:
                            while op_edad!=True:
                                edad=int(input("Ingresa la edad del alumno: "))
                                if edad>-1 and edad<100:
                                    op_edad=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    self.cursor.execute(sql,(edad,j,))
            elif y==4:
                sql = "update alumnos set telefono = %s where dni = %s "
                while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige el dni del alumno que quieres actualizar: "))
                        for i in self.__lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while True:
                        try:
                            while op_tlf!=True:
                                tlf=int(input("Ingresa el teléfono del alumno: "))
                                if len(tlf)==9:
                                    op_tlf=True
                                else:
                                    print("Error, el valor introduccido es incorrecto, intentelo de nuevo...")
                            break
                        except ValueError:
                            print("Error, solo se admiten números, intentelo de nuevo...")
                    #Para ejecutar la consulta#
                    self.cursor.execute(sql,(tlf,j,))
            elif y==5:
                sql = "update alumnos set correo = %s where dni = %s "
                while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=int(input("Elige el dni del alumno que quieres actualizar: "))
                        for i in self.__lista:
                            if int(i)==j:
                                op=True
                                break
                if op_fallo!=True:  
                    while op_correo!=True:
                        correo=input("Ingresa el correo electrónico del alumno: ")
                        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
                            op_correo=True
                        else:
                            print("Error, el correo introduccido no es correcto")
                    #Para ejecutar la consulta#
                    self.cursor.execute(sql,(correo,j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  self.cursor.fetchone()
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Eliminar(self):
        try:
            self.Conexion_BD()
            #consulta sql#
            op=False
            op_fallo=False
            sql = "delete from alumnos where dni = %s "
            while op!=True:
                self.Buscar()
                if not self.__lista:
                    print("Esta vacío")
                    op=True
                    op_fallo=True
                    break
                else:
                    j=input("Elige el dni del alumno que quieres eliminar: ")
                    for i in self.__lista:
                        if i==j:
                            op=True
                            break
            if op_fallo!=True:
                #Para ejecutar la consulta#
                self.cursor.execute(sql,(j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  self.cursor.fetchone()
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")
    def Buscar_Correo(self):
        try:
            self.Conexion_BD()
            #consulta sql#
            op=False
            sql="select correo from alumnos where dni = %s"
            while op!=True:
                    self.Buscar()
                    if not self.__lista:
                        print("Esta vacío")
                        op=True
                        op_fallo=True
                        break
                    else:
                        j=input("Elige el dni del alumno al que le quiere mandar el mensaje: ")
                        for i in self.__lista:
                            if i==j:
                                op=True
                                break
            #Para ejecutar la consulta#
            self.cursor.execute(sql,(j,))
            #Guardamos el resutlado en la variable y la mostramos#
            resultados =  self.cursor.fetchone()
            return resultados
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()
        except mysql.connector.Error:
            print("Error, no se pudo conectar con la base de datos")