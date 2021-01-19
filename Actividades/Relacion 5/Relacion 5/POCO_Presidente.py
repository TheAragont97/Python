class POCO_Presidente:
    def __init__(self,dni,nombre,apellidos,fec_nacimiento,ano_presidente,nom_presidente):
        self.__dni=null
        self.__nombre=null
        self.__apellidos=null
        self.__fec_nacimiento=null
        self.__ano_presidente=null
        self.__nom_equipo=null

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_fec_nacimiento(self):
        return self.__fec_nacimiento

    def set_fec_nacimiento(self, fec_nacimiento):
        self.__fec_nacimiento = fec_nacimiento

    def get_ano_presidente(self):
        return self.__ano_presidente

    def set_ano_presidente(self, ano_presidente):
        self.__ano_presidente = ano_presidente

    def get_nom_equipo(self):
        return self.__nom_equipo

    def set_nom_equipo(self, nom_equipo):
        self.__nom_equipo = nom_equipo