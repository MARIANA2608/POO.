import json

# Clase Producto: Representa los artículos dentro del inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Cada producto tiene un identificador único, un nombre, una cantidad y un precio
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        # Muestra los detalles del producto de forma clara al imprimir
        return f"ID: {self.id_producto} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def a_diccionario(self):
        # Convierte el producto en un diccionario para facilitar la serialización
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

# Clase Inventario: Gestiona los productos utilizando un diccionario
class Inventario:
    def __init__(self):
        # Usamos un diccionario donde las claves son los IDs de los productos
        self.productos = {}

    def agregar_producto(self, producto):
        # Agrega un producto si no existe un producto con el mismo ID
        if producto.id_producto in self.productos:
            print("⚠️ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"✅ Producto '{producto.nombre}' añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto si el ID está registrado
        if id_producto in self.productos:
            producto_eliminado = self.productos.pop(id_producto)
            print(f"🗑️ Producto '{producto_eliminado.nombre}' eliminado del inventario.")
        else:
            print("❌ Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto existente
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"🔄 Producto '{producto.nombre}' actualizado con éxito.")
        else:
            print("❌ Error: No se puede actualizar un producto que no existe.")

    def buscar_por_nombre(self, nombre):
        # Busca productos que coincidan con el nombre (sin distinguir mayúsculas/minúsculas)
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            print("🔍 Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Muestra todos los productos del inventario
        if self.productos:
            print("📦 Inventario Completo:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("📭 El inventario está vacío.")

    def guardar_en_archivo(self, archivo):
        # Guarda el inventario actual en un archivo JSON
        try:
            with open(archivo, 'w') as f:
                json.dump([p.a_diccionario() for p in self.productos.values()], f, indent=4)
            print("💾 Inventario guardado exitosamente.")
        except Exception as e:
            print(f"❌ Error al guardar el archivo: {e}")

    def cargar_desde_archivo(self, archivo):
        # Carga el inventario desde un archivo JSON
        try:
            with open(archivo, 'r') as f:
                productos = json.load(f)
                for p in productos:
                    self.agregar_producto(Producto(**p))
            print("📂 Inventario cargado correctamente.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"❌ Error al cargar el archivo: {e}")

# Función principal: Menú interactivo para gestionar el inventario
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo('inventario.json')

    # Productos predefinidos al iniciar el programa si el archivo no existe
    if not inventario.productos:
        print("📥 Cargando inventario inicial...")
        productos_iniciales = [
            Producto("001", "Laptop", 10, 750.00),
            Producto("002", "Mouse", 50, 25.00),
            Producto("003", "Teclado", 30, 45.50),
            Producto("004", "Monitor", 20, 150.75),
            Producto("005", "Auriculares", 40, 60.00)
        ]
        for p in productos_iniciales:
            inventario.agregar_producto(p)

    while True:
        print("\n📊 Sistema Avanzado de Gestión de Inventarios")
        print("1. Añadir un nuevo producto")
        print("2. Eliminar un producto")
        print("3. Actualizar un producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("🔢 Elige una opción: ")

        if opcion == '1':
            id_producto = input("🆔 Introduce el ID del producto: ")
            nombre = input("📛 Nombre del producto: ")
            try:
                cantidad = int(input("📦 Cantidad disponible: "))
                precio = float(input("💰 Precio del producto: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("❌ Error: Asegúrate de ingresar valores numéricos para cantidad y precio.")

        elif opcion == '2':
            id_producto = input("🆔 ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("🆔 ID del producto a actualizar: ")
            cantidad = input("📦 Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("💰 Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == '4':
            nombre = input("📛 Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            inventario.guardar_en_archivo('inventario.json')
            print("👋 ¡Gracias por usar el sistema de gestión de inventarios!")
            break

        else:
            print("❌ Opción no válida. Por favor, elige una opción del menú.")

if __name__ == '__main__':
    menu()
