frase = input("Introduce una frase: ")
contador = 0
for letra in frase:
    letra2 = "la"
    if letra in letra2:
        contador += 1
print("El número de veces que aparece la letra 'a' es:", contador)