# Clase que representa a un estudiante de la academia de música.
class Estudiante:
    def __init__(self, nombre, instrumento):
        """
        Inicializa los atributos del estudiante.
        - nombre: Nombre del estudiante.
        - instrumento: Instrumento que está aprendiendo (ejemplo: guitarra, piano).
        """
        self.nombre = nombre
        self.instrumento = instrumento
        self.clases_recibidas = 0  # Contador de clases tomadas.

    def tomar_clase(self):
        """Incrementa el contador de clases recibidas por el estudiante."""
        self.clases_recibidas += 1
        return f"{self.nombre} ha tomado una nueva clase de {self.instrumento}. Total: {self.clases_recibidas} clases."

    def mostrar_progreso(self):
        """Muestra el progreso del estudiante basado en el número de clases tomadas."""
        return f"{self.nombre} ha tomado {self.clases_recibidas} clases de {self.instrumento}. ¡Sigue practicando!"

# Clase que gestiona el sistema de la academia.
class AcademiaMusica:
    def __init__(self):
        """Inicializa la academia con una lista vacía de estudiantes registrados."""
        self.estudiantes = []

    def registrar_estudiante(self, estudiante):
        """
        Registra a un estudiante en la academia.
        - estudiante: Objeto de tipo Estudiante.
        """
        self.estudiantes.append(estudiante)
        print(f"El estudiante {estudiante.nombre}, que estudia {estudiante.instrumento}, ha sido registrado.")

    def listar_estudiantes(self):
        """Muestra la lista de estudiantes registrados en la academia."""
        if self.estudiantes:
            print("Estudiantes registrados en la academia:")
            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre} (Instrumento: {estudiante.instrumento})")
        else:
            print("No hay estudiantes registrados en la academia.")

# Ejemplo práctico del sistema
if __name__ == "__main__":
    # Creamos la academia
    academia = AcademiaMusica()

    # Creamos estudiantes
    estudiante1 = Estudiante("Sofía", "Guitarra")
    estudiante2 = Estudiante("Mateo", "Piano")

    # Registramos a los estudiantes
    academia.registrar_estudiante(estudiante1)
    academia.registrar_estudiante(estudiante2)

    # Listamos los estudiantes
    academia.listar_estudiantes()

    # Los estudiantes toman clases
    print(estudiante1.tomar_clase())
    print(estudiante2.tomar_clase())
    print(estudiante2.tomar_clase())

    # Mostramos el progreso de los estudiantes
    print(estudiante1.mostrar_progreso())
    print(estudiante2.mostrar_progreso())
