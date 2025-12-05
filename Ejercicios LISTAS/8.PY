palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")
