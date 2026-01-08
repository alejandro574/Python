asignaturas = ["Matemticas", "Fisica", "Quimica", "Historia", "Lengua"]
suspensas = []
for asignatura in asignaturas:
    nota = float(input("dime la nota de" + asignatura))
    if nota < 5:
        suspensas.append(asignatura)
for asignatura in suspensas:
    print("tienes que repetir",asignatura)
