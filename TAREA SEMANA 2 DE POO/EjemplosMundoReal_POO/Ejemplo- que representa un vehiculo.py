# Clase que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo, matricula):
        # Inicialización de los atributos del vehículo
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.disponible = True  # Por defecto, todos los vehículos están disponibles

    def reservar(self):
        """Marca el vehículo como reservado."""
        if self.disponible:
            self.disponible = False
            return f"El vehículo {self.marca} {self.modelo} con matrícula {self.matricula} ha sido reservado."
        else:
            return "Este vehículo ya está reservado."

    def devolver(self):
        """Marca el vehículo como disponible."""
        if not self.disponible:
            self.disponible = True
            return f"El vehículo {self.marca} {self.modelo} con matrícula {self.matricula} ahora está disponible."
        else:
            return "El vehículo ya está disponible."

# Clase que gestiona el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.vehiculos = []  # Lista de vehículos disponibles en el sistema

    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo al sistema."""
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} añadido al sistema.")

    def listar_vehiculos_disponibles(self):
        """Lista todos los vehículos disponibles para reservar."""
        disponibles = [v for v in self.vehiculos if v.disponible]
        if disponibles:
            print("Vehículos disponibles para reserva:")
            for v in disponibles:
                print(f"- {v.marca} {v.modelo} ({v.matricula})")
        else:
            print("No hay vehículos disponibles en este momento.")

# Uso del sistema
sistema = SistemaReservas()

# Creación de vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla", "ABC123")
vehiculo2 = Vehiculo("Chevrolet", "Spark", "XYZ789")

# Agregar vehículos al sistema
sistema.agregar_vehiculo(vehiculo1)
sistema.agregar_vehiculo(vehiculo2)

# Listar vehículos disponibles
sistema.listar_vehiculos_disponibles()

# Reservar un vehículo
print(vehiculo1.reservar())

# Intentar reservar el mismo vehículo de nuevo
print(vehiculo1.reservar())

# Devolver el vehículo
print(vehiculo1.devolver())

# Listar vehículos disponibles nuevamente
sistema.listar_vehiculos_disponibles()
