class Inventario:
    def __init__(self):
        """
        Constructor que inicializa la lista de productos vacía.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario si no existe un producto con el mismo ID.
        :param producto: Objeto de tipo Producto.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("¡Error! El ID del producto ya existe. No se puede agregar.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido al inventario exitosamente.")

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto del inventario por su ID.
        :param producto_id: ID único del producto a eliminar.
        """
        for p in self.productos:
            if p.get_id() == producto_id:
                self.productos.remove(p)
                print(f"Producto con ID {producto_id} ha sido eliminado.")
                return
        print(f"No se encontró el producto con ID {producto_id}.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        :param producto_id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        for p in self.productos:
            if p.get_id() == producto_id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto con ID {producto_id} actualizado exitosamente.")
                return
        print(f"No se encontró el producto con ID {producto_id}.")

    def buscar_producto(self, nombre):
        """
        Busca productos en el inventario por nombre. Puede ser parcial.
        :param nombre: Nombre del producto o parte del nombre.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")
        else:
            print(f"No se encontraron productos que coincidan con '{nombre}'.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío. ¡Agrega productos primero!")
        else:
            for p in self.productos:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: {p.get_precio()}")
