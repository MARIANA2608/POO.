# Esta función recoge las temperaturas de cada día de la semana directamente del usuario
def registrar_temperaturas():
    temperaturas = []
    print("Por favor, ingresa la temperatura de cada día de la semana:")
    for dia in range(7):
        temp = float(input(f"- Día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Esta función toma las temperaturas almacenadas y calcula el promedio
def calcular_promedio_semanal(temperaturas):
    suma = sum(temperaturas)  # Suma total de las temperaturas
    cantidad = len(temperaturas)  # Total de días
    promedio = suma / cantidad
    return promedio

# Función principal que organiza el flujo del programa
def programa_principal():
    print("Bienvenido al programa de cálculo del promedio semanal del clima.")
    temperaturas = registrar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"\nEl promedio semanal de las temperaturas ingresadas es: {promedio:.2f} °C")

# Ejecutamos el programa principal solo si este archivo es el que se está ejecutando directamente
if __name__ == "__main__":
    programa_principal()
