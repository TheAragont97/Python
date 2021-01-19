from POCO_Notas import *
class Comprobar_Notas:
    def __init__(self):
        self.__inst=POCO_Notas()
    def Comprobar_dni(self,dni):
        if len(dni)==9:
            if dni[:-1].isnumeric()==True:
                if dni[-1:].isnumeric()==True:
                    print("Error, El último dígito tiene que ser una letra")
                    return False
                else:
                    self.__inst.set_dni(dni.upper())
                    return True
            else:
                print("Error, Los ocho primeros dígitos tienen que ser números")
                return False
        else:
            print("Error, tiene que tener 9 carácteres")
            return False
    def Comprobar_notas1(self,notas1):
        if notas1>=0 and notas1<=10:
            self.__inst.set_notas1(notas1)
            return True
        else:
            print("Error, la nota intrucida es incorrecta")
            return False
    def Comprobar_notas2(self,notas2):
        if notas2>=0 and notas2<=10:
            self.__inst.set_notas2(notas2)
            return True
        else:
            print("Error, la nota intrucida es incorrecta")
            return False

