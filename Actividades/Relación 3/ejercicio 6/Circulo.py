import functools, math
class Circulo:
    def __init__(self, radio):
        self.radio=radio
    def get_radio(self):
        return self.radio
    def set_radio(self, radio):
        self.radio = radio
    def comprobacion(self):
        comp=True
        if self.get_radio()<1:
            print("El valor del radio no puede ser ni 0 ni números negativos")
            comp=False
        return comp
    def area(self):
        a=math.pi*(self.get_radio()*self.get_radio())
        return a
    def perimetro(self):
        p=2*math.pi*self.get_radio()
        return p

