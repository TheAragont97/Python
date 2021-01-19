class POCO_Alumno:
    def __init__(self):
        self.__dni="00000000A"
        self.__nombre=""
        self.__dir=""
        self.__edad=18
        self.__tlf=666666666
        self.__beca=True
    
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_dir(self):
        return self.__dir

    def set_dir(self, dir):
        self.__dir = dir

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
     
    def get_tlf(self):
        return self.__tlf

    def set_tlf(self, tlf):
        self.__tlf = tlf

    def get_beca(self):
        return self.__beca

    def set_beca(self, beca):
        self.__beca = beca

