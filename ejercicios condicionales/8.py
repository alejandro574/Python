puntuacion = float(input ("Dime la puntuacion obtenida: "))
if puntuacion == 0:
    print ("Inaceptable")
    print ("Cantidad de dinero = 0")
elif puntuacion == 0.4:
    print ("Aceptable")
    dinero = 2400 * puntuacion
    print ("Cantidad de dinero =", dinero)
elif puntuacion >= 0.6:
    print ("Meritorio")
    dinero = 2400 * puntuacion
    print ("Cantidad de dinero =", dinero)