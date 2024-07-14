#Registro de usuario 1 y 2 
def registro():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electronico: ")
    pin = input("Ingrese su pin: ")
   
    print("Su nombre de la cuenta es:", nombre)
    print("Su correo electronico es:", correo)
    print("Su pin es:", pin)

def segundo():
    segundo = int(input("Desea crear un segundo usuario? (1 para sí, 0 para no): "))
    if segundo == 1:
        nombre2 = input("Ingrese su nombre: ")
        correo2 = input("Ingrese su correo electronico: ")
        pin2 = input("Ingrese su pin: ")

        print("El nombre de la cuenta es:", nombre2)
        print("El correo electronico es:", correo2)
        print("El pin es:", pin2)
    else:
        print("No se creo un segundo usuario")
# verificacion
def verificacion ():
    nombre = ""
    correo = ""
    pin = ""
    nombre2 = ""
    correo2 = ""
    pin2 = ""
    if (nombre == "" and nombre2 ==""):
        print ("No hay ningún usuario registrado por el momento")
        nuevoUsuario = int(input("¿Desea registrar un nuevo usuario?\n1.Si\n2.No: "))
        if nuevoUsuario == 1:
            registro()
            if nombre  != "":
                print("1: ", nombre)
                if nombre2 != "":
                    print("2." + nombre)
                seleU = int(input("Seleccione uno de los usuario:"))
                if seleU == 1:
                    autenticacion1()
                elif seleU == 2 and nombre2 != "":
                            autenticacion2()
                else:
                    print("Selección inválida")
        else: 
            print("Ha salido del sistema")
    else:
        print ("Existen usuarios registrados")
        if nombre!= "":
            print("1: ",nombre)
        if nombre2!= "":
            print("2: ",nombre2)
        seleU = int(input("Seleccione uno de los usuarios: "))
        if seleU == 1:
            autenticacion1()
        if seleU == 2:
            autenticacion2()

#Autenticacion por separado
def autenticacion1 ():
    pinR = ""
    while pinR == pin:
        pinR= int(input("Ingrese el pin del usuario"))
        if pinR != pin:
            print("Contraseña incorrecta")
        elif pinR == pin: 
            print ("Contraseña correcta")
            
def autenticacion2():
        pinR = ""
    while pinR == pin2:
        pinR= int(input("Ingrese el pin del usuario"))
        if pinR != pin2:
            print("Contraseña incorrecta")
        elif pinR == pin2: 
            print ("Contraseña correcta")
# Llamado
registro()
segundo()
