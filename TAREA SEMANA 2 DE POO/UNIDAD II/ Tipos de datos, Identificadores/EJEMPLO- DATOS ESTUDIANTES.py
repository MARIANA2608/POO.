# Programa para registrar datos de estudiantes
# El programa pide el nombre, la edad y la calificación de un estudiante y muestra estos datos al final.

# Función para registrar los datos del estudiante
def registrar_estudiante():
    """
    Solicita al usuario el nombre, la edad y la calificación de un estudiante,
    y devuelve estos datos en un diccionario.
    """
    nombre = input("Ingrese el nombre del estudiante: ")  # Pedimos el nombre
    edad_str = input("Ingrese la edad del estudiante: ")  # Pedimos la edad
    calificacion_str = input("Ingrese la calificación final del estudiante: ")  # Pedimos la calificación

    try:
        edad = int(edad_str)  # Convertimos la edad a entero
        calificacion = float(calificacion_str)  # Convertimos la calificación a flotante

        estudiante = {
            'nombre': nombre,
            'edad': edad,
            'calificacion': calificacion
        }

        return estudiante
    except ValueError:  # Si la edad o la calificación no son números válidos
        print("Por favor, ingresa valores válidos para la edad y la calificación.")
        return None


# Función para mostrar los datos del estudiante
def mostrar_datos_estudiante(estudiante):
    """
    Muestra los datos del estudiante: nombre, edad y calificación.
    """
    if estudiante is not None:
        print(f"\nDatos del estudiante:")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Calificación final: {estudiante['calificacion']:.2f}")
    else:
        print("No se pudo mostrar los datos, ya que no son válidos.")


# Función principal
def main():
    """
    Función principal que controla el flujo del programa. Llama a las funciones
    de registro y visualización de datos.
    """
    estudiante = registrar_estudiante()  # Obtenemos los datos del estudiante
    mostrar_datos_estudiante(estudiante)  # Mostramos los datos del estudiante


# Ejecutamos el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal
