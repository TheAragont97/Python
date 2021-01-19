import functools
class Rectangulo:
    def __init__(self,altura,base):
        self.altura=altura
        self.base=base
    def get_altura(self):
        return self.altura
    def set_altura(self, altura):
        self.altura = altura
    def get_base(self):
        return self.base
    def set_base(self, base):
        self.base = base
    def area(self):
        calculo=self.get_base()*self.get_altura()
        return calculo
    def comprobacion(self):
        comp=True
        if self.get_base()<1 or self.get_altura()<1:
            print("El valor de la base o de la altura no puede ser ni 0 ni números negativos")
            comp=False
        return comp



