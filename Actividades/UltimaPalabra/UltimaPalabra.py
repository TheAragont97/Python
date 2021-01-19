def mideString(frase):
    palabras = frase.split()
    
    print(palabras[-1]+":", len(palabras[-1]))

frase = input("Introduce tu frase: ")



mideString(frase)
