import functools
class Calculadora:
    def __init__(self, n1,n2):
        self.set_n1(n1)
        self.set_n2(n2)
    def get_n1(self):
        return self.n1
    def set_n1(self, n1):
        self.n1 = n1
    def get_n2(self):
        return self.n2
    def set_n2(self, n2):
        self.n2 = n2
    def suma(self):
        s=self.get_n1()+self.get_n2()
        return s
    def resta(self):
        r=self.get_n1()-self.get_n2()
        return r
    def multi(self):
        m=self.get_n1()*self.get_n2()
        return m
    def division(self):
        if self.get_n1()!=0 and self.get_n2()!=0:
            d=self.get_n1()/self.get_n2()
            return d
        else:
            print("No se puede dividir entre 0")

