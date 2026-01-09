fruta1=input("dime la fruta")
kg=float(input("dime los kg"))
frutas = {
    'Plátano':'1.35',
    'Manzana':'0.80',
    'Pera':'0.85',
    'Naranja':'0.70'
}
if fruta1 in frutas:
    precio = frutas[fruta1]
    calculo = kg * float(precio)
    print("te va a costar",calculo)
else:
    print("la fruta no está")
    


