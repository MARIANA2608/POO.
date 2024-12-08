class Vehiculo:
    def avanzar(self):
        pass

class Auto(Vehiculo):
    def avanzar(self):
        print("El auto está manejando por la carretera.")

class Bicicleta(Vehiculo):
    def avanzar(self):
        print("La bicicleta está avanzando por el parque.")

# Función que usa polimorfismo
def mover_vehiculos(vehiculos):
    for vehiculo in vehiculos:
        vehiculo.avanzar()

# Uso
mis_vehiculos = [Auto(), Bicicleta()]
mover_vehiculos(mis_vehiculos)
