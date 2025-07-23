# inventario.py

import json

# Lista global para el inventario
inventario = []

# Función para agregar una prenda al inventario
def agregar_prenda(tipo, talla, cantidad, precio):
    prenda = {
        "tipo": tipo,
        "talla": talla,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(prenda)
    print(f"Prenda '{tipo} - Talla {talla}' agregada correctamente.")

# Función para mostrar todo el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO DE ROPA ---")
        for i, prenda in enumerate(inventario, 1):
            print(f"{i}. {prenda['tipo']} - Talla: {prenda['talla']} - "
                  f"Cantidad: {prenda['cantidad']} - Precio: ${prenda['precio']:.2f}")

# Función para eliminar una prenda
def eliminar_prenda(indice):
    if 1 <= indice <= len(inventario):
        eliminada = inventario.pop(indice - 1)
        print(f"Prenda '{eliminada['tipo']} - Talla {eliminada['talla']}' eliminada.")
    else:
        print("Índice inválido.")

# Función para modificar una prenda
def modificar_prenda(indice, tipo, talla, cantidad, precio):
    if 1 <= indice <= len(inventario):
        prenda = inventario[indice - 1]
        prenda.update({"tipo": tipo, "talla": talla, "cantidad": cantidad, "precio": precio})
        print("Prenda modificada correctamente.")
    else:
        print("Índice inválido.")

# Función para buscar una prenda por tipo o talla
def buscar_prenda(criterio):
    criterio = criterio.strip().lower()
    resultados = [p for p in inventario if criterio in p['tipo'].lower() or criterio in p['talla'].lower()]
    return resultados

# Función para guardar el inventario en un archivo
def guardar_inventario():
    try:
        with open("inventario_ropa.json", "w", encoding="utf-8") as f:
            json.dump(inventario, f, ensure_ascii=False, indent=2)
        print("Inventario guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")

# Función para cargar el inventario desde un archivo
def cargar_inventario():
    global inventario
    try:
        with open("inventario_ropa.json", "r", encoding="utf-8") as f:
            inventario = json.load(f)
        print("Inventario cargado correctamente.")
    except FileNotFoundError:
        print("No existe un archivo de inventario guardado.")
    except Exception as e:
        print(f"Error al cargar: {e}")