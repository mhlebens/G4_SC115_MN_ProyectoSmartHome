# Variables de Almacenamiento de datos
usuarios = []
casas = []
def registro_usuarios():
    nombre=input("Ingrese su nombre: ")
    correo=input("Ingrese su correo electronico: ")
    pin =input("Ingrese su pin: ")
   
    print("Su nombre de la cuenta es: ",nombre)
    print("Su nombre de la cuenta es: ",correo)
    print("Su pin es: ",pin)
    

def verificacion_usuariosregistrados():
    if usuarios:
        print("Usuarios que se encuentran registrados:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario['nombre']} ")
        return True
    else:
        print("No hay usuarios registrados. Por favor, registre un nuevo usuario.")
        return False

def autenticacion_usuario():
    if not usuarios:
        print("No hay usuarios registrados.")
        return None
    
    print("Seleccione un usuario:")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario['nombre']}")
    seleccion = int(input("Seleccione el número de usuario: ")) - 1
    usuario_seleccionado = usuarios[seleccion]

    while True:
        pin = input("Ingrese su PIN: ")
        if pin == usuario_seleccionado['pin']:
            print("Autenticación exitosa.\n")
            return usuario_seleccionado
        else:
            print("PIN incorrecto. Intente de nuevo.\n")

# Función principal del programa
def main():
    while True:
        print("¡Bienvenido a SmartHome!.")
        if not verificación_usuariosregistrados():
            registrar_usuarios()
        
        usuario = autenticacion_usuario()
        if not usuario:
            continue
        
        while True:
            if not mostrar_casas(usuario):
                registrar_casa(usuario)
            else:
                print("\nOpciones: \n1. Registrar nueva casa\n2. Seleccionar casa existente\n3. Cerrar sesión")
                opcion = input("Seleccione una opción: ")
                if opcion == '1':
                    registrar_casa(usuario)
                elif opcion == '2':
                    casa_seleccionada = input("Ingrese el nombre de la casa seleccionada: ")
                    if casa_seleccionada not in casas:
                        print(f"No existe una casa con el nombre {casa_seleccionada}.\n")
                        continue
                    
                    while True:
                        if not mostrar_habitaciones(casa_seleccionada):
                            registrar_habitacion(casa_seleccionada)
                        else:
                            print("\nOpciones: \n1. Registrar nueva habitación\n2. Volver a selección de casa\n3. Cerrar sesión")
                            opcion = input("Seleccione una opción: ")
                            if opcion == '1':
                                registrar_habitacion(casa_seleccionada)
                            elif opcion == '2':
                                break
                            elif opcion == '3':
                                return
                elif opcion == '3':
                    break

if __name__ == "__main__":
    main()
