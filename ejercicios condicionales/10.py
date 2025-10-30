pizza = str(input("Quieres una pizza vegetariana"))
if pizza == "si":
    print ("Has elegido la pizza vegetariana")
    elige1 = input ("Elige 1 de estos ingredientes para tu pizza: Pimiento y Tofu ")
    if elige1 == "Pimiento":
         print ("Tiene los siguientes ingredientes","Mozzarela,Tomate,")
    else:
            print ("Tiene los siguientes ingredientes","Mozzarela,Tomate,Tofu")
else:
    print ("Has elegido la pizza NO  vegetariana")
    elige2 = input ("Elige 1 de estos ingredientes para tu pizza: Peperoni, Jamón y Salmón ")
    if elige2 == "Peperoni":
         print ("Tiene los siguientes ingredientes","Mozzarela,Tomate,Peperoni")
    elif elige2 == "Jamón":
            print ("Tiene los siguientes ingredientes","Mozzarela,Tomate,Jamón")
    else:
            print ("Tiene los siguientes ingredientes","Mozzarela,Tomate,Salmón")

