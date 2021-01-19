import smtplib, socket, sys, getpass #Todos estos import son necesarios para poder utilizar las funciones 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
 
# Conexion con el servidor 
	try:
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587) #Este ejemplo como podéis ver está empleando una cuenta gmail
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		print( "Conexión exitosa con Gmail")
		print("Conectado a Gmail")
		# Datos 
		try:
			gmail_user = str(input("Escriba su correo: ")).lower().strip()
			gmail_pwd = getpass.getpass("Escriba su password: ").strip() #Empleamos la función getpass para evitar que nuestro password se vea
			smtpserver.login(gmail_user, gmail_pwd)
		except smtplib.SMTPException:
			print("")
			print ("Autenticación incorrecta" + "\n")
			smtpserver.close()
			getpass.getpass("Presione ENTER para continuar...")
			sys.exit(1)
	except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
		print("Fallo en la conexión con Gmail")		
		print("Presione ENTER para continuar...")
		sys.exit(1)
 
 
	while True:
		to = str(input("Enviar correo a: ")).lower().strip()
		if to != "":
			break
		else:
			print( "El correo es necesario!!!")
 
	sub = str(input("Asunto: ")).strip()
	bodymsg = str(input("Mensaje: "))
	
	enviar = MIMEMultipart() #Creamos un objeto MIMEMultipart para crear el correo y que contenga todos los elementos propios de un correo 
	enviar['From'] = gmail_user #El emisor del correo, quién lo manda
	enviar['To'] = to #El destinatario del correo, a quién va dirigido
	enviar['Subject'] = sub #El asunto del correo
	enviar.attach(MIMEText(bodymsg)) #El texto del correo
	try:
		smtpserver.sendmail(gmail_user, to, str(enviar))
	except smtplib.SMTPException:
		print( "El correo no pudo ser enviado" + "\n")
		smtpserver.close()
		getpass.getpass("Presione ENTER para continuar...")
		sys.exit(1)
 
	print ("El correo se envió correctamente" + "\n")	
	smtpserver.close()
	getpass.getpass("Presione ENTER para continuar")
	sys.exit(1)
 
 
main()
