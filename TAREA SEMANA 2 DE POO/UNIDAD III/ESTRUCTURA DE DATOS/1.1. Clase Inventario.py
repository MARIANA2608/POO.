class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        """
        Constructor que inicializa los atributos del producto.
        :param producto_id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad del producto en inventario.
        :param precio: Precio del producto.
        """
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        """Devuelve el ID del producto."""
        return self.producto_id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad del producto disponible."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    def set_nombre(self, nombre):
        """Actualiza el nombre del producto."""
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Actualiza el precio del producto."""
        self.precio = precio
