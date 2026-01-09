nombre = input("Dime tu nombre")
edad = input("Dime tu edad")
direccion = input("Dime tu direccion")
telefono = input("Dime tu telefono")
usuario = {
    'nombre': nombre,
    'edad': edad,
    'dirección': direccion,
    'teléfono' : telefono
}
print (usuario['nombre']," tiene", usuario['edad'] ," años, vive en", usuario['dirección']," y su número de teléfono es", usuario['teléfono'])