class POCO_Partidos:
    def __init__(self,cod_partido,momento_gol,fecha,gol_casa,gol_fuera):
        self.__cod_partido=null
        self.__momento_gol=null
        self.__fecha=null
        self.__gol_casa=null
        self.__gol_fuera=null

    def get_cod_partido(self):
        return self.__cod_partido

    def set_cod_partido(self, cod_partido):
        self.__cod_partido = cod_partido

    def get_momento_gol(self):
        return self.__momento_gol

    def set_momento_gol(self, momento_gol):
        self.__momento_gol = momento_gol

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_gol_casa(self):
        return self.__gol_casa

    def set_gol_casa(self, gol_casa):
        self.__gol_casa= gol_casa

    def get_gol_fuera(self):
        return self.__gol_fuera

    def set_gol_fuera(self, gol_fuera):
        self.__gol_fuera= gol_fuera