rentaanual = float(input("Introduce la renta anual: "))
if rentaanual < 10000:
 print ("El tipo impositivo es del 5%")
elif rentaanual >= 10000 and rentaanual < 20000:
   print ("El tipo impositivo es del 15%")
    
elif rentaanual >= 20000 and rentaanual < 35000:    
    print ("El tipo impositivo es del 20%")
elif rentaanual >= 35000 and rentaanual < 60000:
 print ("El tipo impositivo es del 30%")
else:
 print ("El tipo impositivo es del 45%")


   
