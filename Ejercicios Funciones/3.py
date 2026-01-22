def factorial(numero):
    resultado = 1
    while numero >= 1:
        resultado = resultado * numero
        numero = numero -1
    return resultado
print(factorial(3))