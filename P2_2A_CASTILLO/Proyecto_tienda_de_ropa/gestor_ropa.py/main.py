# main.py

import inventario

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n-------- \U0001F4DD MENÚ --------")
    print("_" * 25)
    print("1. \U0001F4DD Agregar prenda")
    print("2. \U0001F4DD Mostrar inventario")
    print("3. \U0001F4DB Eliminar prenda")
    print("4. \U0001F501 Modificar prenda")
    print("5. \U0001F50D Buscar prenda")
    print("6. \u2705 Guardar inventario")
    print("7. \U0001F501 Cargar inventario")
    print("8. \U0001F6AA Salir")

# Función principal que ejecuta el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de prenda (ej. Camisa, Pantalón): ")
            talla = input("Talla (S, M, L, XL): ")
            cantidad = int(input("Cantidad  de prendas disponibles: "))
            precio = float(input("Precio unitario: $  "))
            inventario.agregar_prenda(tipo, talla, cantidad, precio)

        elif opcion == "2":
            inventario.mostrar_inventario()

        elif opcion == "3":
            inventario.mostrar_inventario()
            if inventario.inventario:
                indice = int(input("Número de la prenda a eliminar: "))
                inventario.eliminar_prenda(indice)

        elif opcion == "4":
            inventario.mostrar_inventario()
            if inventario.inventario:
                indice = int(input("Número de la prenda a modificar: "))
                tipo = input("Nuevo tipo: ")
                talla = input("Nueva talla (S, M, L, XL): ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: $ "))
                inventario.modificar_prenda(indice, tipo, talla, cantidad, precio)

        elif opcion == "5":
            criterio = input("Buscar por tipo o talla: ")
            resultados = inventario.buscar_prenda(criterio)
            if resultados:
                print("\n--- RESULTADOS DE BÚSQUEDA ---")
                for i, prenda in enumerate(resultados, 1):
                    print(f"{i}. {prenda['tipo']} - Talla: {prenda['talla']} - "
                          f"Cantidad: {prenda['cantidad']} - Precio: ${prenda['precio']:.2f}")
            else:
                print("No se encontraron prendas con ese criterio.")

        elif opcion == "6":
            inventario.guardar_inventario()

        elif opcion == "7":
            inventario.cargar_inventario()

        elif opcion == "8":
            print("\U0001F6AA Saliendo del programa.")
            break

        else:
            print(" \u26A0 Opción inválida.")

if __name__ == "__main__":
    main()
