# Función para registrar un usuario
def registro():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    pin = input("Ingrese su pin: ")
    
    print("Su nombre de la cuenta es:", nombre)
    print("Su correo electrónico es:", correo)
    print("Su pin es:", pin)
    return nombre, correo, pin

# Función para registrar un segundo usuario
def segundo():
    segundo = int(input("Desea crear un segundo usuario? (1 para sí, 0 para no): "))
    if segundo == 1:
        nombre2 = input("Ingrese su nombre: ")
        correo2 = input("Ingrese su correo electrónico: ")
        pin2 = input("Ingrese su pin: ")

        print("El nombre de la cuenta es:", nombre2)
        print("El correo electrónico es:", correo2)
        print("El pin es:", pin2)
        return nombre2, correo2, pin2
    else:
        print("No se creó un segundo usuario")
        return None, None, None

# Verificación de usuarios registrados
def verificacion(nombre, correo, pin, nombre2, correo2, pin2):
    if nombre == "" and nombre2 == "":
        print("No hay ningún usuario registrado por el momento")
        nuevoUsuario = int(input("¿Desea registrar un nuevo usuario?\n1. Sí\n2. No: "))
        if nuevoUsuario == 1:
            nombre, correo, pin = registro()
            if nombre != "":
                print("1:", nombre)
                if nombre2 != "":
                    print("2:", nombre2)
                seleU = int(input("Seleccione uno de los usuarios: "))
                if seleU == 1:
                    autenticacion(pin)
                elif seleU == 2 and nombre2 != "":
                    autenticacion(pin2)
                else:
                    print("Selección inválida")
        else:
            print("Ha salido del sistema")
    else:
        print("Existen usuarios registrados")
        if nombre != "":
            print("1:", nombre)
        if nombre2 != "":
            print("2:", nombre2)
        seleU = int(input("Seleccione uno de los usuarios: "))
        if seleU == 1:
            autenticacion(pin)
        elif seleU == 2:
            autenticacion(pin2)

# Autenticación de usuario
def autenticacion(pin):
    pinR = ""
    while pinR != pin:
        pinR = input("Ingrese el pin del usuario: ")
        if pinR != pin:
            print("Contraseña incorrecta")
        else:
            print("Contraseña correcta")

# Llamado a las funciones de registro y verificación
nombre, correo, pin = registro()
nombre2, correo2, pin2 = segundo()

# Verificación de usuarios registrados
verificacion(nombre, correo, pin, nombre2, correo2, pin2)

# Registro y gestión de casas y habitaciones
def gestionar_casas():
    # Ingresar a sistema previo a crear casas y registrar habitaciones
    usuario = input("Ingrese su usuario: ")
    correo = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")
    
    # Registrar casa
    registrar_casa = ""
    
    # Ciclo para registrar casas
    while True:
        casaMenu = int(input("Seleccione la casa preferida\n1.Registrar Casa#1\n2.Registrar casa#2\n3.Salir\nDigite la opción que desea: "))
        if casaMenu == 1:
            if registrar_casa == "":
                registrar_casa = input("Registre Casa#1: ")
                print("Casa#1 registrada")
        elif casaMenu == 2:
            registrar_casa = input("Registre Casa#2: ")
            print("Casa#2 registrada")
        elif casaMenu == 3:
            print("Ha salido del sistema")
            break
        else:
            print("La opción seleccionada no corresponde")

    # Agregar sala, dormitorio y comedor en casa
    agregar_sala = ""
    agregar_dormitorio = ""
    agregar_comedor = ""

    # Ciclo para agregar áreas a la casa
    while True:
        opcionMenu = int(input("Seleccione la opción que desea\n1.Agregar una sala\n2.Agregar un dormitorio\n3.Agregar comedor\n4.Salir\nDigite la opción que desea: "))
        if opcionMenu == 1:
            if agregar_sala == "":
                agregar_sala = input("Agregue una sala: ")
                print("Sala agregada")
        elif opcionMenu == 2:
            agregar_dormitorio = input("Agregue un dormitorio: ")
            print("Dormitorio agregado")
        elif opcionMenu == 3:
            agregar_comedor = input("Agregue un comedor: ")
            print("Comedor agregado")
        elif opcionMenu == 4:
            print("Ha salido del sistema")
            break
        else:
            print("La opción seleccionada no corresponde")

    # Agregar sala, dormitorio, baño y cochera en la casa
    agregar_baño = ""
    agregar_cochera = ""

    # Ciclo para agregar más áreas a la casa
    while True:
        opcionMenu = int(input("Seleccione la opción que desea\n1.Agregar una sala\n2.Agregar un dormitorio\n3.Agregar baño\n4.Agregar cochera\n5.Salir\nDigite la opción que desea: "))
        if opcionMenu == 1:
            if agregar_sala == "":
                agregar_sala = input("Agregue una sala: ")
                print("Sala agregada")
        elif opcionMenu == 2:
            agregar_dormitorio = input("Agregue un dormitorio: ")
            print("Dormitorio agregado")
        elif opcionMenu == 3:
            agregar_baño = input("Agregue un baño: ")
            print("Baño agregado")
        elif opcionMenu == 4:
            agregar_cochera = input("Agregue una cochera: ")
            print("Cochera agregada")
        elif opcionMenu == 5:
            print("Ha salido del sistema")
            break
        else:
            print("La opción seleccionada no corresponde")

# Llamado a la función de gestión de casas
gestionar_casas()
