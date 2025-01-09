# Programa para calcular el área de un círculo
# Este programa solicita al usuario el radio de un círculo y calcula su área utilizando la fórmula A = π * r^2

import math  # Importamos la librería 'math' para usar la constante pi


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: A = π * r^2
    """
    area = math.pi * radio ** 2  # Usamos la constante pi y calculamos el área
    return area


# Función para obtener el radio del usuario
def obtener_radio():
    """
    Solicita al usuario el radio del círculo y lo valida.
    Si el valor ingresado no es válido, pide al usuario que ingrese un valor correcto.
    """
    radio_str = input("Por favor, ingresa el radio del círculo: ")

    try:
        radio = float(radio_str)  # Convertimos la entrada del usuario a un número flotante
        if radio <= 0:  # Verificamos que el radio sea un número positivo
            print("¡El radio debe ser un número positivo!")
            return None
        return radio
    except ValueError:  # En caso de que el usuario ingrese un valor no numérico
        print("¡Por favor, ingresa un número válido!")
        return None


# Función principal que organiza el flujo del programa
def main():
    """
    Función principal que controla el flujo del programa: obtiene el radio,
    calcula el área y muestra el resultado.
    """
    radio = obtener_radio()  # Llamamos a la función para obtener el radio del usuario

    if radio is not None:  # Si el radio es válido
        area = calcular_area_circulo(radio)  # Calculamos el área usando la función definida
        print(f"El área del círculo con radio {radio} es: {area:.2f}")  # Mostramos el resultado con dos decimales


# Ejecutamos el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para que el programa se ejecute
