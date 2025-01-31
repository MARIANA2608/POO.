import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD I/EjemplosMundoReal_POO/Ejemplo- estudiante academia.py',
        '2': 'UNIDAD I/EjemplosMundoReal_POO/Ejemplo- mascota veterinaria.py',
        '3': 'UNIDAD I/EjemplosMundoReal_POO/Ejemplo- que representa un vehiculo.py',
        '4': 'UNIDAD I/EjemplosMundoReal_POO/Ejemplo-pedido en la cafeteria.py',
        '5': 'UNIDAD I/Programacion tradicional frente a POO/Programación Orientada a Objetos (POO)/Programación Orientada a Objetos (POO).py',
        '6': 'UNIDAD I/Programacion tradicional frente a POO/Programación Tradicional/Programación Tradicional.py',
        '7': 'UNIDAD I/Programacion tradicional frente a POO/Texto Comparativo/Texto Comparativo',
        '8': 'UNIDAD I/Tecnicas de Programacion/ABSTRACCION/ABSTRACCION.py',
        '9': 'UNIDAD I/Tecnicas de Programacion/ENCAPSULACION/ENCAPSULACION.py',
        '10': 'UNIDAD I/Tecnicas de Programacion/HERENCIA/AHERENCIA.py',
        '11': 'UNIDAD I/Tecnicas de Programacion/POLIFORMISMO/POLIFORMISMO.py',
        '12': 'UNIDAD II/ Tipos de datos, Identificadores/EJEMPLO- CONVERSION TEMPERATURA.py',
        '13': 'UNIDAD II/ Tipos de datos, Identificadores/EJEMPLO- DATOS ESTUDIANTES.py',
        '14': 'UNIDAD II/ Tipos de datos, Identificadores/EJEMPLO-CALCULAR AREA CIRCULO.py',
        '15': 'UNIDAD II/Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/EJEMPLO DE Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo.py',
        '16': 'UNIDAD II/CONSTRUCTORES Y DESTRUCTORES/EJEMPLO CONSTRUCTORES Y DESTRUCTORES.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()