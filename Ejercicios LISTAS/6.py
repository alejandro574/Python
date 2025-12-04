asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspensas = []   
for asignatura in asignaturas:
    nota = float(input("Nota de " + asignatura + ": "))
    if nota < 5:              
        suspensas.append(asignatura)
print("Tienes que repetir:", suspensas)
