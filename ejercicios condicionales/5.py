edad = input("Ingrese su edad: ")
ingresosmensulaes = input("Ingrese sus ingresos mensuales: ")
if int(edad) >= 16:
    if int(ingresosmensulaes) >= 1000:
        print("Usted debe tributar.")
    else:
        print("Usted no debe tributar.")
