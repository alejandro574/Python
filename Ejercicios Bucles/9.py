contraseña = "admin"
while(True):
    contraseña_usuario = input("Dime la contraseña: ")
    if contraseña_usuario == contraseña:
        print("Contraseña correcta")
        break
    else:   
        print("Contraseña incorrecta, inténtalo de nuevo.")