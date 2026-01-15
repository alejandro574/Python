fecha = input("dime la fecha formato dd/mm/aaaa ")
fecha1 = fecha.split("/")
meses = {
    "01":"ENERO",
    "02":"Febrero",
    "03":"Marzo",
    "04":"Abril",
    "05":"Mayo",
    "06":"Junio",
    "07":"Julio",
    "08":"Agosto",
    "09":"Septiembre",
    "10":"Octubre",
    "11":"Noviembre",
    "12":"Diciembre",
}
mese2=fecha1[1]  
if fecha1[1] in meses:
    print(fecha1[0],"de",meses[mese2],fecha1[2])
