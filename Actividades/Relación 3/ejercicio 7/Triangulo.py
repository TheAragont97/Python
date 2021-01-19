import functools
class Triangulo:
    def __init__(self, lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def get_lado1(self):
        return self.lado1
    def set_lado1(self, lado1):
        self.lado1 = lado1
    def get_lado2(self):
        return self.lado2
    def set_lado2(self, lado2):
        self.lado2 = lado2
    def get_lado3(self):
        return self.lado3
    def set_lado3(self, lado3):
        self.lado3 = lado3
    def lado_mayor(self):
        if self.get_lado1()>self.get_lado2():
            if self.get_lado1()>self.get_lado3():
                print("El lado mayor es",self.get_lado1())
            else:
                print("El lado mayor es",self.get_lado3())
        else:
            if self.get_lado2()>self.get_lado3():
                print("El lado mayor es",self.get_lado2())
            else:
                print("El lado mayor es ",self.get_lado3())
    def tipo(self):
        if self.get_lado1()==self.get_lado2() and self.get_lado2()==self.get_lado3() and self.get_lado1()==self.get_lado3():
            print("Es un triángulo equilátero, tiene todos los lados iguales")
        elif self.get_lado1()!=self.get_lado2() and self.get_lado2()!=self.get_lado3() and self.get_lado1()!=self.get_lado3():
            print("Es un triángulo escaleno, tiene todos los lados desicuales")
        else:
            print("Es un triángulo isósceles, tiene dos lados iguales y uno desigual al resto")
    def comprobacion(self):
        comp=True
        if self.get_lado1()<1 or self.get_lado2()<1 or self.get_lado3()<1:
            print("El valor de la base o de la altura no puede ser ni 0 ni números negativos")
            comp=False
        return comp
            


