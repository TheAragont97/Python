f=open("empleados.xml",'r')
nombre=""
apellidos=""
for linea in f:
    linea = linea.lstrip().rstrip()
    if linea.startswith("<nombre>"):
        nombre=linea[8:-9]
    if linea.startswith("<apellidos>"):
        apellidos=linea[11:-12]
        print("Nombre: "+ nombre+ " " +apellidos )