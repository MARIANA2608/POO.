import os

class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        """Devuelve la representación en texto del producto para escribir en el archivo"""
        return f"{self.codigo},{self.nombre},{self.cantidad}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo si existe, o crea uno nuevo si no está presente."""
        if not os.path.exists(self.archivo):
            try:
                open(self.archivo, 'w').close()  # Crea el archivo si no existe
                print("ℹ️ El archivo de inventario no existía. Se ha creado uno nuevo.")
            except PermissionError:
                print("❌ Error: No tienes permisos para crear el archivo.")
                return

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:  # Ignorar líneas vacías
                        try:
                            codigo, nombre, cantidad = linea.split(',')
                            self.productos[codigo] = Producto(codigo, nombre, int(cantidad))
                        except ValueError:
                            print(f"⚠️ Advertencia: Línea con formato incorrecto omitida. Línea: {linea}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"❌ Error al acceder al archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda el inventario completo en el archivo de texto."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("✅ Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, codigo, nombre, cantidad):
        """Añade un nuevo producto al inventario."""
        if codigo in self.productos:
            print("⚠️ El producto ya existe. Usa la opción de actualizar.")
            return
        self.productos[codigo] = Producto(codigo, nombre, cantidad)
        self.guardar_en_archivo()
        print(f"✅ Producto '{nombre}' añadido exitosamente.")

    def actualizar_producto(self, codigo, cantidad):
        """Actualiza la cantidad de un producto existente."""
        if codigo not in self.productos:
            print("❌ Producto no encontrado.")
            return
        self.productos[codigo].cantidad = cantidad
        self.guardar_en_archivo()
        print(f"🔄 Producto '{self.productos[codigo].nombre}' actualizado a {cantidad} unidades.")

    def eliminar_producto(self, codigo):
        """Elimina un producto del inventario."""
        if codigo not in self.productos:
            print("❌ Producto no encontrado.")
            return
        nombre = self.productos[codigo].nombre
        del self.productos[codigo]
        self.guardar_en_archivo()
        print(f"🗑️ Producto '{nombre}' eliminado del inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("📭 El inventario está vacío.")
            return
        print("📦 Inventario Actual:")
        for producto in self.productos.values():
            print(f"- {producto.nombre} (Código: {producto.codigo}) - Cantidad: {producto.cantidad}")


def menu():
    inventario = Inventario()

    while True:
        print("\n📊 Sistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                inventario.agregar_producto(codigo, nombre, cantidad)
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero.")

        elif opcion == '2':
            codigo = input("Ingrese el código del producto a actualizar: ")
            try:
                cantidad = int(input("Ingrese la nueva cantidad: "))
                inventario.actualizar_producto(codigo, cantidad)
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero.")

        elif opcion == '3':
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
