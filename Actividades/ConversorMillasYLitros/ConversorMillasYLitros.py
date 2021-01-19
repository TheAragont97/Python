milla_metros = 1609.344
galon_litros = 3.785411784
def l100kmtompg(litros):
    return (((galon_litros/milla_metros)/litros)*100000)
 
def mpgtol100km(millas):
    return (((galon_litros/milla_metros)/millas)*100000)
 
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
