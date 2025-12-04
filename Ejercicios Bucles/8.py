#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
numeroentero = int(input("Introduce un número entero positivo: "))
for i in range(1, numeroentero ):
    print(' ' * (numeroentero - i) + '*' * i)
