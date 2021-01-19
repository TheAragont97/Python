class POCO_Jugador:
    def __init__(self,cod_jugador,nombre,fecha_nac,posicion):
        self.__cod_jugador=null
        self.__nombre=null
        self.__fecha_nac=null
        self.__posicion=null

    def get_cod_jugador(self):
        return self.__cod_jugador

    def set_cod_jugador(self, cod_jugador):
        self.__cod_jugador = cod_jugador

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_fecha_nac(self):
        return self.__fecha_nac

    def set_fecha_nac(self, fecha_nac):
        self.__fecha_nac = fecha_nac

    def get_posicion(self):
        return self.__posicion

    def set_posicion(self, posicion):
        self.__posicion = posicion

