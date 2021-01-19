class POCO_Notas:
    def __init__(self):
        self.__dni="00000000A"
        self.__notas1=5
        self.__notas2=5

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_notas1(self):
        return self.__notas1

    def set_notas1(self, notas1):
        self.__notas1 = notas1

    def get_notas2(self):
        return self.__notas2

    def set_notas2(self, notas2):
        self.__notas2 = notas2