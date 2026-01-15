creditos={
    'Matemáticas': 6, 
    'Física': 4,
    'Química': 5
}
contar = 0
for credito in creditos:
    creditos2= (creditos[credito])
    print("La asignatura",credito,"tiene",creditos2)
    contar = contar + creditos2

print(contar)
