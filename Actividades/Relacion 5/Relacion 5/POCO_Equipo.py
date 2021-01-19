class POCO_Equipo:
    def __init__(self,cod_equipo,cod_jugador,dni_presidente,cod_partido,nombre,estadio,aforo,fundacion,ciudad):
        self.__cod_equipo=null
        self.__cod_jugador=null
        self.__dni_presidente=null 
        self.__cod_partido=null 
        self.__nombre=null 
        self.__estadio=null 
        self.__aforo=null 
        self.__fundacion=null 
        self.__ciudad=null 

    def get_cod_equipo(self):
        return self.__cod_equipo

    def set_cod_equipo(self, cod_equipo):
        self.__cod_equipo = cod_equipo

    def get_cod_jugador(self):
        return self.__cod_jugador

    def set_cod_jugador(self, cod_jugador):
        self.__cod_jugador = cod_jugador

    def get_dni_presidente(self):
        return self.__dni_presidente

    def set_dni_presidente(self, dni_presidente):
        self.__dni_presidente = dni_presidente

    def get_cod_partido(self):
        return self.__cod_partido

    def set_cod_partido(self, cod_partido):
        self.__cod_partido = cod_partido

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_estadio(self):
        return self.__estadio

    def set_estadio(self, estadio):
        self.__estadio = estadio

    def get_aforo(self):
        return self.__aforo

    def set_aforo(self, aforo):
        self.__aforo = aforo

    def get_fundacion(self):
        return self.__fundacion

    def set_fundacion(self, fundacion):
        self.__fundacion = fundacion

    def get_ciudad(self):
        return self.__ciudad

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad