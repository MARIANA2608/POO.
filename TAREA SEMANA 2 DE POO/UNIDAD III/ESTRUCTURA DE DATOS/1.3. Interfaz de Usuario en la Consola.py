# Clase Producto
class Producto:
    # Código de la clase Producto como ya te lo proporcioné
    pass

# Clase Inventario
class Inventario:
    # Código de la clase Inventario como ya te lo proporcioné
    pass

# Menú interactivo y función principal
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()  # Aquí se crea el objeto inventario

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar vacío si no quiere cambiarla): ")
            precio = input("Ingrese el nuevo precio (dejar vacío si no quiere cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("¡Gracias por usar el sistema! Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción correcta.")

if __name__ == "__main__":
    main()
