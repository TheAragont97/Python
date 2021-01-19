import functools
class ToNumber:
    def __init__(self,romano):
        self.romano=romano
    def conversion(self,romano):
        if romano.isnumeric() == True:
            print("Error, no puede ser un número")
        else:
            romanos={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
            entero = 0
            for i in range(len(romano)):
                    if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
                        entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
                    else:
                        entero+=romanos[romano[i]]
            print("Este es tu número entero:  ",entero)