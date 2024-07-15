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


#Tercera tarea(Raymundo), la idea de esta parte del proyecto es crear una proceso para agregar  casas y habitaciones( se considera que es necesario agregar, areas de la casa, como sala, dormitorio y comedor), para ello, se crean 3 variables para luego crear un ciclo, donde el usuario, al tener su casa, pueda ir creando las areas de su casa, para ello, se propone un ciclo, donde le consultara que area de la casa quiere agregar y con option de salir del sistema, para correr este proceso, primero tienen que ingresar con su usuario, pw y correo

## Ingresar a sistema previo a crear casas y registrar habitaciones
Ingresar_a_sistema = ""

if Ingresar_a_sistema =="":
        usuario = input("Ingrese su usuario:")
        Correo = input("Ingrese su correo")
        password = input("Ingrese su contraseña")
        
## Registrar casa
## Se crean 1 variable

Registrar_casa = ""

##Se crea un ciclo para registrar casas
casaMenu=1

while   casaMenu !=3:
    casaMenu = int(input("Seleccione la casa preferida\n1.Registrar Casa#1\n2.Registrar casa#2\n3.Salir\nDigite la opcion que desea:"))
    if casaMenu ==1:
        if Registrar_casa =="":
            print("Registre Casa#1")
           
        
    elif casaMenu ==2:
        Registrar_casa = input("Registre casa#2")
        print("Registre Casa#2")

                  
    elif casaMenu ==3:
        print("Ha salido del sistema")

    else:
        print("La opción seleccionada no corresponde")


##Agregar sala, dormitorio y comedor en casa        
## Se crean 3 variables
agregar_sala = ""
agregar_dormitorio =""
agregar_comedor = ""

##  Se trabaja en un ciclo para que el usuario elija la opcion en su casa a agregar
opcionMenu=1

while opcionMenu !=4:

    opcionMenu = int(input("Seleccione la opción que desea\n1.Agregar una sala\n2.Agregar un dormitorio\n3.Agregar comedor\n4.Salir\nDigite la opción que desea:"))

    if opcionMenu ==1:
        if agregar_sala =="":
            print("Agregue una sala")
            
            
            
    elif opcionMenu ==2:
        agregar_dormitorio = input("Agregue un dormitorio:")
        print("Dormitorio agregado")
        
    elif opcionMenu ==3:
        agregar_comedor = input("Agregue comedor:")
        print("Comedor agregado")

    elif opcionMenu ==4:
        print("Ha salido del sistema")

    else:
        print("La opción seleccionada no corresponde")
## Se crean 1 variable

Registrar_habitaciones = ""

##Agregar sala, dormitorio , baño y cochera  en la casa
## Se crean 3 variables
agregar_sala = ""
agregar_dormitorio =""
agregar_baño = ""
Agregar_cochera = ""

##  Se trabaja en un ciclo para que el usuario elija la opcion en su casa a agregar
opcionMenu=1

while opcionMenu !=4:

    opcionMenu = int(input("Seleccione la opción que desea\n1.Agregar una sala\n2.Agregar un dormitorio\n3.Agregar baño \n4. Agregar cochera \ n5.salir n Digite la opción que desea:"))

    if opcionMenu ==1:
        if agregar_sala =="":
            print("Agregue una sala")
            
            
            
    elif opcionMenu ==2:
        agregar_dormitorio = input("Agregue un dormitorio:")
        print("Dormitorio agregado")
        
    elif opcionMenu ==3:
        agregar_comedor = input("Agregue un baño:")
        print("Comedor agregado")

    elif opcionMenu ==4:
       agregar_cochera = input("Agregue la cochera :")
        print("Comedor agregado")

 elif opcionMenu ==5:
        print("Ha salido del sistema")


    else:
        print("La opción seleccionada no disponible ")
