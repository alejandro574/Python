peso = input("¿Cuál es tu peso? ")
estatura = input("¿Cuál es tu estatura en metros? ")
inidice = float(peso) / float(estatura)**2
print("Tu índice de masa corporal redondeado es: ", round(inidice, 2))