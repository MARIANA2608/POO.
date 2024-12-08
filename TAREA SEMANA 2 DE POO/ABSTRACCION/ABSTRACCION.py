from abc import ABC, abstractmethod

# Clase abstracta que define las acciones esenciales de una máquina de café
class MaquinaDeCafe(ABC):
    @abstractmethod
    def preparar_cafe(self, tipo):
        pass

    @abstractmethod
    def mostrar_menu(self):
        pass

# Implementación de la máquina de café
class MiCafetera(MaquinaDeCafe):
    def __init__(self):
        self.__menu = {"Espresso": 1.5, "Cappuccino": 2.0, "Latte": 2.5}

    def preparar_cafe(self, tipo):
        if tipo in self.__menu:
            print(f"Preparando tu {tipo}... ¡Disfrútalo!")
        else:
            print(f"Lo siento, no ofrecemos {tipo}.")

    def mostrar_menu(self):
        print("Menú de la Cafetera:")
        for cafe, precio in self.__menu.items():
            print(f"- {cafe}: ${precio}")

# Uso de la máquina
cafetera = MiCafetera()
cafetera.mostrar_menu()
cafetera.preparar_cafe("Espresso")
cafetera.preparar_cafe("Americano")  # Este no está en el menú
