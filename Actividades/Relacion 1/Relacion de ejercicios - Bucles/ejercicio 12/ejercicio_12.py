frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
cont = 0
for i in frase:
    if i == letra:
        cont += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, cont, frase))
