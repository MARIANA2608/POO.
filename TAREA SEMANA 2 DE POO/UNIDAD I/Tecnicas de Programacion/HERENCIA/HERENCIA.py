# Clase base
class Electrodomestico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"Encendiendo el {self.modelo} de la marca {self.marca}.")

# Clase derivada
class Lavadora(Electrodomestico):
    def lavar(self):
        print("La lavadora está limpiando la ropa.")

# Clase derivada
class Microondas(Electrodomestico):
    def calentar(self):
        print("El microondas está calentando la comida.")

# Uso
mi_lavadora = Lavadora("LG", "TurboWash 360")
mi_microondas = Microondas("Samsung", "QuickHeat 900")

mi_lavadora.encender()
mi_lavadora.lavar()

mi_microondas.encender()
mi_microondas.calentar()
