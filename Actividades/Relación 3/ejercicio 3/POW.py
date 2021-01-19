import functools
class POW:
    def __init__(self, base, exp):
        self.base=base
        self.exp=exp
    def calculo(self, base, exp):
        cal=1.0
        if self.exp>0:
            for i in range(self.exp):
                cal=cal*self.base
        elif self.exp<=-1:
            for i in range(-self.exp):
                cal=cal/self.base
        else:
            cal=1.0
        print("El resultado de elevar a ",self.exp," el número ",self.base," es ",cal)

