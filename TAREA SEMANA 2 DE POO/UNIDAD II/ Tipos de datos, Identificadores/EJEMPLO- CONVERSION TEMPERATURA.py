# Programa para convertir temperaturas de Celsius a Fahrenheit
# El programa pide al usuario una temperatura en Celsius y la convierte a Fahrenheit utilizando la fórmula F = (C * 9/5) + 32

# Función para convertir de Celsius a Fahrenheit
def convertir_a_fahrenheit(temperatura_celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32  # Aplicamos la fórmula de conversión
    return temperatura_fahrenheit


# Función para solicitar la temperatura al usuario
def obtener_temperatura_celsius():
    """
    Solicita al usuario que ingrese una temperatura en Celsius.
    Si la entrada no es válida, solicita nuevamente la temperatura.
    """
    temperatura_str = input("Ingresa la temperatura en grados Celsius: ")

    try:
        temperatura_celsius = float(temperatura_str)  # Convertimos la entrada a número flotante
        return temperatura_celsius
    except ValueError:  # Si el valor ingresado no es válido
        print("Por favor, ingresa un número válido para la temperatura.")
        return None


# Función principal
def main():
    """
    Función principal que obtiene la temperatura del usuario, la convierte y muestra el resultado.
    """
    temperatura_celsius = obtener_temperatura_celsius()  # Obtenemos la temperatura de Celsius

    if temperatura_celsius is not None:  # Si el valor ingresado es válido
        temperatura_fahrenheit = convertir_a_fahrenheit(temperatura_celsius)  # Convertimos a Fahrenheit
        print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit:.2f} grados Fahrenheit.")


# Ejecutamos el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal
