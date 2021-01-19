import functools
class Palabra:
    def __init__(self,cadena):
        self.cadena=cadena
    def get_string(self,cadena):
        if self.cadena.isnumeric() == True:
            return True
        else:
            return False
    def print_string(self):
        if self.get_string(self.cadena)==False:
            print(self.cadena.upper())
        else:
            print("Error, se ha encontrado carácteres numéricos a la cadena")
