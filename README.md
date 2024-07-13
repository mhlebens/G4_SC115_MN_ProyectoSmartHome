# G4_SC115_MN_ProyectoSmartHome


#Tercera tarea(Raymundo), la idea de esta parte del proyecto es crear una proceso para agregar habitaciones( se considera que es necesario agregar, areas de la casa, como sala, dormitorio y comedor), para ello, se crean 3 variables para luego crear un ciclo, donde el usuario, al tener su casa, pueda ir creando las areas de su casa, para ello, se propone un ciclo, donde le consultara que area de la casa quiere agregar y con option de salir del sistema.

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
