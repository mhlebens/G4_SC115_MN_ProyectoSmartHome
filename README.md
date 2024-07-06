# G4_SC115_MN_ProyectoSmartHome


#Tercera tarea(Raymundo), la idea de esta parte del proyecto es crear una estructura de datos para almacenar informacion de las casas, como crear una funcion que le permita al usuario registrar una nueva casa, se crea una "clase" llamada casa, para luego crear funciones para agregar habitaciones ( esty considerando un tamano de cada habitacion, donde las habitaciones creadas, como escenario, les llame,  "Sala", "Cocina" y un "dormitorio", se pueden agregar mas), esto con la idea de dar un output o print para el usuario, sobre lo agregado (** en validacion**)

class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = {}

    def agregar_habitacion(self, nombre_habitacion, metros_cuadrados):
        self.habitaciones[nombre_habitacion] = metros_cuadrados

# Crear una casa
mi_casa = Casa("Mi Casa")

# Agregar habitaciones a la casa
mi_casa.agregar_habitacion("Sala", 30)
mi_casa.agregar_habitacion("Cocina", 20)
mi_casa.agregar_habitacion("Dormitorio", 15)

# Imprimir las habitaciones de la casa
print(f"Habitaciones de la casa {mi_casa.nombre}:")
for habitacion, metros_cuadrados in mi_casa.habitaciones.items():
    print(f"{habitacion}: {metros_cuadrados} metros cuadrados")
