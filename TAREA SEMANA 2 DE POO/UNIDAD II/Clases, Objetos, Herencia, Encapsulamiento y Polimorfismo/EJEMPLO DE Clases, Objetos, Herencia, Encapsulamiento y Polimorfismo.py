# Clase base que representa un dispositivo electrónico genérico
# Esta clase será la base para las clases derivadas, demostrando el concepto de herencia.
class DispositivoElectronico:
    def __init__(self, marca, modelo, precio):
        # Encapsulación: Los atributos son privados para proteger los datos sensibles del dispositivo.
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Método público para mostrar información básica del dispositivo
    def mostrar_info(self):
        return f"Dispositivo: Marca: {self.__marca}, Modelo: {self.__modelo}, Precio: ${self.__precio:.2f}"

    # Método público para simular el encendido del dispositivo
    def encender(self):
        return f"El dispositivo {self.__marca} modelo {self.__modelo} está encendiéndose."

# Clase derivada que representa un teléfono inteligente
# Aquí se aplica herencia al extender la funcionalidad de la clase base.
class TelefonoInteligente(DispositivoElectronico):
    def __init__(self, marca, modelo, precio, sistema_operativo):
        # Llamada al constructor de la clase base para reutilizar atributos.
        super().__init__(marca, modelo, precio)
        self.sistema_operativo = sistema_operativo

    # Polimorfismo: Sobrescribe el método mostrar_info para incluir información adicional.
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Sistema Operativo: {self.sistema_operativo}"

    # Polimorfismo: Personaliza el comportamiento del método encender.
    def encender(self):
        return f"El teléfono con {self.sistema_operativo} se está iniciando. ¡Bienvenido!"

    # Método único de esta clase para instalar aplicaciones
    def instalar_app(self, nombre_app):
        return f"La aplicación '{nombre_app}' se ha instalado correctamente en tu dispositivo."

# Clase derivada que representa una laptop
# También extiende la funcionalidad de la clase base, aplicando herencia.
class Laptop(DispositivoElectronico):
    def __init__(self, marca, modelo, precio, tamaño_pantalla):
        # Reutilizamos el constructor de la clase base para atributos comunes.
        super().__init__(marca, modelo, precio)
        self.tamaño_pantalla = tamaño_pantalla

    # Polimorfismo: Sobrescribe el método mostrar_info para agregar detalles de la pantalla.
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tamaño de Pantalla: {self.tamaño_pantalla} pulgadas"

    # Polimorfismo: Personaliza el método encender con un mensaje específico para laptops.
    def encender(self):
        return f"La laptop con pantalla de {self.tamaño_pantalla} pulgadas está lista para usarse."

# Función principal para demostrar cómo funcionan las clases y sus conceptos de POO
def main():
    # Creamos un dispositivo genérico para demostrar la clase base
    dispositivo = DispositivoElectronico("Sony", "Alpha", 1200.00)

    # Creamos un teléfono inteligente, utilizando la clase derivada
    telefono = TelefonoInteligente("Samsung", "Galaxy S23", 999.99, "Android")

    # Creamos una laptop, utilizando la otra clase derivada
    laptop = Laptop("Apple", "MacBook Air", 1500.00, 13.3)

    # Usamos los métodos de cada clase para demostrar encapsulación, herencia y polimorfismo
    print(dispositivo.mostrar_info())  # Clase base
    print(dispositivo.encender())  # Clase base

    print(telefono.mostrar_info())  # Clase derivada: sobrescritura (polimorfismo)
    print(telefono.encender())  # Clase derivada: sobrescritura (polimorfismo)
    print(telefono.instalar_app("WhatsApp"))  # Método exclusivo de TelefonoInteligente

    print(laptop.mostrar_info())  # Clase derivada: sobrescritura (polimorfismo)
    print(laptop.encender())  # Clase derivada: sobrescritura (polimorfismo)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
