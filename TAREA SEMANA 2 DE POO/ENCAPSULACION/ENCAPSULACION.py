class TarjetaDeCredito:
    def __init__(self, numero, titular, limite):
        self.__numero = numero  # Dato privado
        self.__titular = titular
        self.__limite = limite
        self.__saldo = 0  # Comienza sin deudas

    def realizar_compra(self, monto):
        if monto <= (self.__limite - self.__saldo):
            self.__saldo += monto
            print(f"Compra aprobada por ${monto}. Saldo actual: ${self.__saldo}")
        else:
            print(f"Compra rechazada. Excede el límite disponible de ${self.__limite - self.__saldo}.")

    def mostrar_informacion(self):
        print(f"Titular: {self.__titular}, Límite: ${self.__limite}, Saldo: ${self.__saldo}")

# Uso
mi_tarjeta = TarjetaDeCredito("1234-5678-9876-5432", "María García", 1000)
mi_tarjeta.mostrar_informacion()
mi_tarjeta.realizar_compra(300)
mi_tarjeta.realizar_compra(800)  # Esto excede el límite
