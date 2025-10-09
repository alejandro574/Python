cantidad = input("ingresa una cantidad para invertir : ")
interes = input("ingresa el interes anual (en porcentaje): ")
años = input("ingresa la cantidad de años: ")
capital = float(cantidad) * (1 + float(interes) / 100) ** int(años)
print (capital)



