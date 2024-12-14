class RegistroClima:
    def __init__(self):
        # Inicializamos una lista para almacenar las temperaturas
        self.temperaturas = []

    # Método para registrar temperaturas diarias
    def registrar_temperaturas(self):
        print("Vamos a registrar las temperaturas diarias:")
        for dia in range(7):
            temp = float(input(f"- Ingresa la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio_semanal(self):
        if not self.temperaturas:
            print("No hay temperaturas registradas para calcular el promedio.")
            return None
        suma = sum(self.temperaturas)  # Suma de todas las temperaturas
        promedio = suma / len(self.temperaturas)  # Dividimos por el número de días
        return promedio

# Función principal que organiza la interacción con el programa
def programa_principal():
    print("¡Hola! Este es tu programa para calcular el promedio semanal del clima.")
    clima = RegistroClima()  # Creamos un objeto de la clase RegistroClima
    clima.registrar_temperaturas()
    promedio = clima.calcular_promedio_semanal()

    # Verificamos si se obtuvo un promedio válido antes de mostrarlo
    if promedio is not None:
        print(f"\nEl promedio semanal de las temperaturas registradas es: {promedio:.2f} °C")

# Verificamos si este archivo es el ejecutado directamente
if __name__ == "__main__":
    programa_principal()
