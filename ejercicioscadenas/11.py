#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
nombre = input("dime el nombre del producto")
precio = float(input("dime el precio del producto"))
unidades = int(input("dime las unidades"))
coste = float(precio * unidades)
print ("El producto es: ", nombre)
print ("El precio unitario es: {:06.2f} euros".format(precio))
print ("El número de unidades es: {:03d}".format(unidades)) 
print ("El coste total es: {:08.2f} euros".format(coste))

