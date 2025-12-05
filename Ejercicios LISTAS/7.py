abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
resultado = []
posicion = 1
for letra in abecedario:
    if posicion % 3 != 0:  
        resultado.append(letra)
    posicion += 1
print(resultado)
