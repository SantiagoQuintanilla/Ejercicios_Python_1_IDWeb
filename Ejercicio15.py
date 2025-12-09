def mostrar_inventario(inventario):
    print("\n--- Inventario Completo ---")
    for producto in inventario:
        print(f"{producto}: {inventario[producto]} unidades")
    print()


def agregar_o_actualizar(inventario):
    producto = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad a agregar: "))

    if producto in inventario:
        print(f"El producto '{producto}' ya existe. Cantidad anterior: {inventario[producto]}")
        inventario[producto] += cantidad
        print(f"Cantidad actualizada: {inventario[producto]}")
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")


def buscar_producto(inventario):
    producto = input("Ingrese el nombre del producto a buscar: ").lower()
    if producto in inventario:
        print(f"Cantidad disponible de '{producto}': {inventario[producto]}")
    else:
        print(f"El producto '{producto}' no existe en el inventario.")


def menu():
    inventario = {}

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        print("1. Mostrar inventario")
        print("2. Agregar o actualizar producto")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            agregar_o_actualizar(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()