from POCO_Alumno import *
class Comprobar_Alumno:
    def __init__(self):
        self.__inst=POCO_Alumno()
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
    def Comprobar_edad(self,edad):
        if edad>0 and edad<=100:
            self.__inst.set_edad(edad)
            return True
        else:
            print("Error, la edad indicada es incorrecta")
            return False
    def Comprobar_tlf(self,tlf):
        if len(str(tlf))==9:
            self.__inst.set_tlf(tlf)
            return True
        else:
            print("Error, el teléfono introducido no es correcto, tiene que tener 9 números")
            return False
    def Comprobar_nombre(self,nombre):
        if nombre.isnumeric()==False:
            self.__inst.set_nombre(nombre)
            return True
        else:
            print("Error, Solo se admiten letras")
            return False
    def Comprobar_dir(self,dir):
        if dir.isnumeric()==False:
            self.__inst.set_dir(dir)
            return True
        else:
            print("Error, Solo se admiten letras")
            return False
    def Comprobar_beca(self,beca):
        if beca.isnumeric()==False:
            if beca.upper()=="SI":
                self.__inst.set_beca(True)
                return True
            elif beca.upper()=="NO":
                self.__inst.set_beca(False)
                return True
            else:
                print("Opción incorrecta")
                return False
        else:
            print("Error, Solo se admiten letras")
            return False
