# Clase que representa un pedido en la cafetería
class Pedido:
    def __init__(self, cliente, items):
        # Inicialización de atributos del pedido
        self.cliente = cliente
        self.items = items  # Lista de ítems pedidos
        self.estado = "Pendiente"  # Estado inicial del pedido

    def calcular_total(self):
        """Calcula el costo total del pedido."""
        total = sum(item['precio'] for item in self.items)
        return f"Total a pagar por {self.cliente}: ${total:.2f}"

    def marcar_como_entregado(self):
        """Cambia el estado del pedido a entregado."""
        if self.estado == "Pendiente":
            self.estado = "Entregado"
            return f"Pedido de {self.cliente} ha sido entregado."
        else:
            return "El pedido ya fue entregado."


# Clase que representa un ítem del menú
class ItemMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


# Ejemplo de uso
if __name__ == "__main__":
    # Creación de ítems del menú
    cafe = ItemMenu("Café", 1.50)
    sandwich = ItemMenu("Sándwich", 3.75)
    jugo = ItemMenu("Jugo de Naranja", 2.25)

    # Creación de un pedido
    pedido1 = Pedido("Ana", [{"nombre": cafe.nombre, "precio": cafe.precio},
                             {"nombre": sandwich.nombre, "precio": sandwich.precio}])

    # Detalles del pedido
    print(pedido1.calcular_total())

    # Cambiar estado del pedido
    print(pedido1.marcar_como_entregado())
