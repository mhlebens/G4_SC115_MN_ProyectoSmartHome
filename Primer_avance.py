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

# Llamado
registro()
segundo()
