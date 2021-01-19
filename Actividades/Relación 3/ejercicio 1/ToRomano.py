import functools
class ToRomano:
    def __init__(self,entero):
        self.entero=entero
    def conversion(self,entero):
         if self.entero <=0:
            print("Error, No existe ni los números negativos ni el cero en los números romanos")
         else:
            numeros=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
            numerales=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
            numeral=''
            i=0
            # // significa division #
            while self.entero > 0:
                for _ in range(self.entero // numeros[i]):
                    numeral += numerales[i]
                    self.entero -= numeros[i]
                i+=1
            print("Este es el número romano: ",numeral)

       
   


