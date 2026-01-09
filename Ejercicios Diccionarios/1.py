
divisas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}
divisa = input("Introduce una divisa (Euro, Dollar o Yen): ")
if divisa in divisas:
    print("El símbolo es:", divisas[divisa])
else:
    print("La divisa no esta en el diccionario.")
