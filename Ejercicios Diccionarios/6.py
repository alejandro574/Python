vacio={
    "nombre":"",
    "edad":"",
    "sexo":""
}
for vacio1 in vacio:
    variable = input("Dime tu %s"%vacio1)
    vacio[vacio1] = variable
    print (vacio)
    