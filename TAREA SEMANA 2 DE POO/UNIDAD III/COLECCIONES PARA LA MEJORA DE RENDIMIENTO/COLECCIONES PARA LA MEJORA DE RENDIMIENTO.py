import json


# Clase Libro: representa un libro con atributos título, autor, categoría e ISBN.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla para autor y título (no cambia).
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[1]}' de {self.info[0]} ({self.categoria}, ISBN: {self.isbn})"


# Clase Usuario: representa un usuario de la biblioteca con atributos nombre, ID y libros prestados.
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados.

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca: gestiona los libros, usuarios y préstamos.
class Biblioteca:
    def __init__(self, archivo_json):
        self.libros = {}  # Diccionario para almacenar libros con el ISBN como clave.
        self.usuarios = {}  # Diccionario para almacenar usuarios con ID de usuario como clave.
        self.archivo_json = archivo_json
        self.cargar_datos()

    def cargar_datos(self):
        try:
            # Si el archivo existe y no está vacío, cargar los datos.
            with open(self.archivo_json, 'r') as archivo:
                datos = json.load(archivo)
                for libro in datos.get("libros", []):
                    nuevo_libro = Libro(libro["titulo"], libro["autor"], libro["categoria"], libro["isbn"])
                    self.libros[libro["isbn"]] = nuevo_libro
                for usuario in datos.get("usuarios", []):
                    nuevo_usuario = Usuario(usuario["nombre"], usuario["id_usuario"])
                    nuevo_usuario.libros_prestados = usuario.get("libros_prestados", [])
                    self.usuarios[usuario["id_usuario"]] = nuevo_usuario
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o está corrupto, iniciar con una biblioteca vacía.
            print("No se encontró el archivo o está vacío. Se creará una nueva biblioteca.")

    def guardar_datos(self):
        # Guardar los datos actuales de libros y usuarios en el archivo JSON.
        datos = {
            "libros": [{
                "titulo": libro.info[1],
                "autor": libro.info[0],
                "categoria": libro.categoria,
                "isbn": libro.isbn
            } for libro in self.libros.values()],
            "usuarios": [{
                "nombre": usuario.nombre,
                "id_usuario": usuario.id_usuario,
                "libros_prestados": usuario.libros_prestados
            } for usuario in self.usuarios.values()]
        }
        with open(self.archivo_json, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def añadir_libro(self, titulo, autor, categoria, isbn):
        if isbn not in self.libros:
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            self.libros[isbn] = nuevo_libro
            print(f"Libro '{titulo}' añadido.")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuarios:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = nuevo_usuario
            print(f"Usuario '{nombre}' registrado.")
        else:
            print("El usuario ya está registrado.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print("Usuario eliminado.")
        else:
            print("El usuario no existe.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            if isbn not in usuario.libros_prestados:
                usuario.libros_prestados.append(isbn)
                print(f"Libro '{libro.info[1]}' prestado a {usuario.nombre}.")
            else:
                print(f"El usuario ya tiene este libro prestado.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            if isbn in usuario.libros_prestados:
                usuario.libros_prestados.remove(isbn)
                print(f"Libro '{libro.info[1]}' devuelto por {usuario.nombre}.")
            else:
                print("Este libro no fue prestado a este usuario.")
        else:
            print("Libro o usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = []
        if criterio == "titulo":
            encontrados = [libro for libro in self.libros.values() if valor.lower() in libro.info[1].lower()]
        elif criterio == "autor":
            encontrados = [libro for libro in self.libros.values() if valor.lower() in libro.info[0].lower()]
        elif criterio == "categoria":
            encontrados = [libro for libro in self.libros.values() if valor.lower() in libro.categoria.lower()]

        if encontrados:
            print(f"Libros encontrados por {criterio} '{valor}':")
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros por {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for isbn in usuario.libros_prestados:
                    print(self.libros[isbn])
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Función de menú para interactuar con el sistema de biblioteca.
def menu():
    biblioteca = Biblioteca("biblioteca.json")

    while True:
        print("\nMenú de Biblioteca:")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            biblioteca.añadir_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            criterio = input("¿Buscar por título, autor o categoría? ").lower()
            valor = input(f"Ingrese el valor de {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            biblioteca.guardar_datos()
            print("¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


# Ejecutar el menú
menu()
