palabras = {
    "hola":"hello",
    "adios":"bye",
    "perro":"dog"
}
frase = input("DIME UNA FRASE ")
frase2 = frase.split(" ")
frase3=""
for palabra in frase2:
    frase3 = frase3 + palabras[palabra]
    frase3 += (" ")
print (frase3)


    