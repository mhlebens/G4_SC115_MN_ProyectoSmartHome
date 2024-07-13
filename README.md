# G4_SC115_MN_ProyectoSmartHome


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
    casaMenu = int(input("Seleccione la casa preferida\n1.Registrar Casa#1\n2.Registrar casa#2\n4.Salir\nDigite la opcion que desea:"))
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


##Agregar sala, dormitorio y comedor en casa(Parte2_Raymundo)        
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
