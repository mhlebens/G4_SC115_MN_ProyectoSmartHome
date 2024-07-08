# Variables de Almacenamiento de datos
usuarios = []

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

# Main del Programa
def main():
    while True:
        print("¡Bienvenido a la aplicación de Smart Home!")
        if not verificación_usuariosregistrados():
            registrar_usuarios()
        
        usuario = autenticacion_usuario()
        if not usuario:
            continue
