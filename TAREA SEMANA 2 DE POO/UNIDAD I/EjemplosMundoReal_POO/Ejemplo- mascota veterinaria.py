# Esta clase representa una mascota registrada en una veterinaria.
class Mascota:
    def __init__(self, nombre, especie, edad):
        """
        Inicializa los atributos de una mascota.
        - nombre: Nombre de la mascota.
        - especie: Tipo de mascota (ejemplo: perro, gato).
        - edad: Edad de la mascota en años.
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.historial_medico = []  # Lista para guardar citas médicas o tratamientos realizados.

    def agregar_historial(self, descripcion):
        """
        Añade una entrada al historial médico de la mascota.
        - descripcion: Detalle de la consulta o tratamiento.
        """
        self.historial_medico.append(descripcion)
        return f"Se ha añadido al historial de {self.nombre}: {descripcion}"

    def mostrar_historial(self):
        """Muestra el historial médico completo de la mascota."""
        if self.historial_medico:
            historial = "\n".join(self.historial_medico)
            return f"Historial médico de {self.nombre}:\n{historial}"
        else:
            return f"{self.nombre} aún no tiene historial médico registrado."

# Esta clase administra el sistema de la veterinaria.
class Veterinaria:
    def __init__(self):
        """Inicializa una lista vacía de mascotas registradas en la veterinaria."""
        self.mascotas = []

    def registrar_mascota(self, mascota):
        """
        Registra una nueva mascota en la veterinaria.
        - mascota: Objeto de tipo Mascota.
        """
        self.mascotas.append(mascota)
        print(f"La mascota {mascota.nombre}, un {mascota.especie}, ha sido registrada exitosamente.")

    def listar_mascotas(self):
        """Muestra una lista de todas las mascotas registradas en la veterinaria."""
        if self.mascotas:
            print("Mascotas registradas en la veterinaria:")
            for mascota in self.mascotas:
                print(f"- {mascota.nombre} ({mascota.especie}, {mascota.edad} años)")
        else:
            print("No hay mascotas registradas aún.")

# Ejemplo práctico del sistema
if __name__ == "__main__":
    # Creamos la veterinaria
    veterinaria = Veterinaria()

    # Creamos algunas mascotas
    mascota1 = Mascota("Luna", "Perro", 5)
    mascota2 = Mascota("Milo", "Gato", 3)

    # Registramos las mascotas
    veterinaria.registrar_mascota(mascota1)
    veterinaria.registrar_mascota(mascota2)

    # Mostramos las mascotas registradas
    veterinaria.listar_mascotas()

    # Añadimos historial médico a una mascota
    print(mascota1.agregar_historial("Vacunación contra la rabia."))
    print(mascota1.agregar_historial("Consulta por alergias."))

    # Mostramos el historial médico de la mascota
    print(mascota1.mostrar_historial())
