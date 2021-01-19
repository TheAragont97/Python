import smtplib, socket, sys, getpass #Todos estos import son necesarios para poder utilizar las funciones 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Gestion_Alumno import *
import datetime
class Email:
    def __init__(self):
        self.gmail_user=""
        self.enviar=""
        self.to=""
        self.sub=""
        self.bodymsg=""
        self.smtpserver=""
        self.__ga=Gestion_Alumno()
    def Introducir(self):
        # Conexion con el servidor 
        try:
            self.smtpserver = smtplib.SMTP("smtp.gmail.com", 587) #Este ejemplo como podéis ver está empleando una cuenta gmail
            self.smtpserver.ehlo()
            self.smtpserver.starttls()
            self.smtpserver.ehlo()
            print( "Conexión exitosa con Gmail")
            print("Conectado a Gmail")
		    # Datos 
            try:
                self.gmail_user = str(input("Escriba su correo: ")).lower().strip()
                gmail_pwd = getpass.getpass("Escriba su password: ").strip() #Empleamos la función getpass para evitar que nuestro password se vea
                self.smtpserver.login(self.gmail_user, gmail_pwd)
            except smtplib.SMTPException:
                print("")
                print ("Autenticación incorrecta" + "\n")
                self.smtpserver.close()
        except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
            print("Fallo en la conexión con Gmail")
       
    def Enviar_Correo(self):
        while True:
            tupla = self.__ga.Buscar_Correo()
            tupla=str(tupla)
            self.to = tupla[2:-3]
            if self.to != "":
                break
            else:
                print( "El correo es necesario!!!")
 
        self.sub = str(input("Asunto: ")).strip()
        self.bodymsg = str(input("Mensaje: "))
        self.enviar = MIMEMultipart() #Creamos un objeto MIMEMultipart para crear el correo y que contenga todos los elementos propios de un correo 
        self.enviar['From'] = self.gmail_user #El emisor del correo, quién lo manda
        self.enviar['To'] = self.to #El destinatario del correo, a quién va dirigido
        self.enviar['Subject'] = self.sub #El asunto del correo
        self.enviar.attach(MIMEText(self.bodymsg)) #El texto del correo
        
        print ("Datos introducidos correctamente" + "\n")	
        op=0
        while op!=1 and op!=2:
            op=int(input("¿Desea enviar el correo? 1.Si/2.No: "))
            if op==1:
                try:
                    self.smtpserver.sendmail(str(self.gmail_user), str(self.to), str(self.enviar))
                    TIME = datetime.datetime.now()
                    print("Email sent at {}".format(TIME))
                except smtplib.SMTPException:
                    print( "El correo no pudo ser enviado" + "\n")
                    self.smtpserver.close()
            else:
                print("El mensaje no se envió")
        self.smtpserver.close()