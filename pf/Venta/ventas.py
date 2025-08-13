from funciones import *
from datetime import datetime

def menu_ventas():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" GESTIÓN DE VENTAS ".center(50, "="))
        print("=" * 50)
        print("1. Registrar nueva venta")
        print("2. Listar ventas")
        print("3. Buscar venta por fecha")
        print("4. Detalle de venta")
        print("5. Volver al menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            buscar_ventas_fecha()
        elif opcion == "4":
            detalle_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            esperar_tecla()

def registrar_venta():
    limpiar_pantalla()
    print("=" * 50)
    print(" REGISTRAR NUEVA VENTA ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if not conexion:
            return
            
        cursor = conexion.cursor(dictionary=True)
        
        # Listar clientes para selección
        cursor.execute("SELECT id, nombre, apellido FROM clientes ORDER BY apellido, nombre")
        clientes = cursor.fetchall()
        
        if not clientes:
            print("\nNo hay clientes registrados. Debe registrar al menos un cliente.")
            esperar_tecla()
            return
            
        print("\nClientes disponibles:")
        for cliente in clientes:
            print(f"ID: {cliente['id']} - {cliente['nombre']} {cliente['apellido']}")
        
        id_cliente = input("\nIngrese ID del cliente: ")
        
        # Verificar que el cliente existe
        cursor.execute("SELECT id FROM clientes WHERE id = %s", (id_cliente,))
        if not cursor.fetchone():
            print("\nCliente no encontrado.")
            esperar_tecla()
            return
        
        # Listar productos disponibles
        cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE stock > 0 ORDER BY nombre")
        productos = cursor.fetchall()
        
        if not productos:
            print("\nNo hay productos con stock disponible.")
            esperar_tecla()
            return
            
        # Proceso de selección de productos
        items = []
        total = 0.0
        
        while True:
            limpiar_pantalla()
            print("=" * 50)
            print(" SELECCIONAR PRODUCTOS ".center(50, "="))
            print("=" * 50)
            
            print("\nProductos disponibles:")
            for producto in productos:
                print(f"ID: {producto['id']} - {producto['nombre']} - ${producto['precio']:.2f} - Stock: {producto['stock']}")
            
            print("\nProductos seleccionados:")
            if items:
                for idx, item in enumerate(items, 1):
                    producto = next(p for p in productos if p['id'] == item['producto_id'])
                    print(f"{idx}. {producto['nombre']} - {item['cantidad']} x ${producto['precio']:.2f} = ${item['cantidad'] * producto['precio']:.2f}")
                print(f"\nTOTAL PARCIAL: ${total:.2f}")
            else:
                print("No hay productos seleccionados aún.")
            
            print("\n1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Finalizar selección")
            print("4. Cancelar venta")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":  # Agregar producto
                id_producto = input("Ingrese ID del producto a agregar: ")
                producto = next((p for p in productos if str(p['id']) == id_producto), None)
                
                if producto:
                    cantidad = int(input(f"Cantidad de '{producto['nombre']}' (max {producto['stock']}): "))
                    
                    if cantidad <= 0 or cantidad > producto['stock']:
                        print("Cantidad no válida.")
                        esperar_tecla()
                        continue
                        
                    # Verificar si el producto ya está en la lista
                    item_existente = next((item for item in items if item['producto_id'] == producto['id']), None)
                    
                    if item_existente:
                        item_existente['cantidad'] += cantidad
                    else:
                        items.append({
                            'producto_id': producto['id'],
                            'cantidad': cantidad,
                            'precio': producto['precio']
                        })
                    
                    total += cantidad * producto['precio']
                else:
                    print("Producto no encontrado.")
                    esperar_tecla()
                    
            elif opcion == "2" and items:  # Eliminar producto
                num_item = int(input("Número de producto a eliminar: ")) - 1
                
                if 0 <= num_item < len(items):
                    producto = next(p for p in productos if p['id'] == items[num_item]['producto_id'])
                    total -= items[num_item]['cantidad'] * producto['precio']
                    del items[num_item]
                else:
                    print("Número de producto no válido.")
                    esperar_tecla()
                    
            elif opcion == "3" and items:  # Finalizar selección
                break
                
            elif opcion == "4":  # Cancelar venta
                print("\nVenta cancelada.")
                esperar_tecla()
                return
                
            else:
                print("Opción no válida.")
                esperar_tecla()
        
        # Seleccionar método de pago
        print("\nMétodos de pago:")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Transferencia")
        metodo_pago = input("Seleccione método de pago (1-3): ")
        metodos = {1: 'efectivo', 2: 'tarjeta', 3: 'transferencia'}
        metodo_pago = metodos.get(int(metodo_pago), 'efectivo')
        
        # Confirmar venta
        print(f"\nTOTAL A PAGAR: ${total:.2f}")
        confirmacion = input("\n¿Confirmar venta? (s/n): ").lower()
        
        if confirmacion != 's':
            print("\nVenta cancelada.")
            esperar_tecla()
            return
        
        # Registrar la venta
        cursor.execute("INSERT INTO ventas (cliente_id, total, metodo_pago) VALUES (%s, %s, %s)", 
                      (id_cliente, total, metodo_pago))
        venta_id = cursor.lastrowid
        
        # Registrar detalles de venta y actualizar stock
        for item in items:
            cursor.execute("""
                INSERT INTO detalle_venta 
                (venta_id, producto_id, cantidad, precio_unitario) 
                VALUES (%s, %s, %s, %s)
            """, (venta_id, item['producto_id'], item['cantidad'], item['precio']))
            
            cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", 
                         (item['cantidad'], item['producto_id']))
            
            # Registrar movimiento de inventario
            cursor.execute("""
                INSERT INTO inventario 
                (producto_id, tipo, cantidad, motivo, usuario) 
                VALUES (%s, 'salida', %s, 'Venta', 'vendedor')
            """, (item['producto_id'], item['cantidad']))
        
        conexion.commit()
        print(f"\nVenta registrada exitosamente! N° de venta: {venta_id}")
        
    except Error as e:
        print(f"\nError al registrar venta: {e}")
        if 'conexion' in locals() and conexion.is_connected():
            conexion.rollback()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
    
    esperar_tecla()

def listar_ventas():
    limpiar_pantalla()
    print("=" * 50)
    print(" LISTADO DE VENTAS ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT v.id, v.fecha_venta, c.nombre, c.apellido, v.total, v.metodo_pago 
                FROM ventas v
                JOIN clientes c ON v.cliente_id = c.id
                ORDER BY v.fecha_venta DESC
                LIMIT 50
            """)
            ventas = cursor.fetchall()
            
            if ventas:
                for venta in ventas:
                    print(f"\nN° Venta: {venta['id']}")
                    print(f"Fecha: {venta['fecha_venta']}")
                    print(f"Cliente: {venta['nombre']} {venta['apellido']}")
                    print(f"Total: ${venta['total']:.2f}")
                    print(f"Método pago: {venta['metodo_pago'].capitalize()}")
                    print("-" * 50)
            else:
                print("\nNo hay ventas registradas.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al listar ventas: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def buscar_ventas_fecha():
    limpiar_pantalla()
    print("=" * 50)
    print(" BUSCAR VENTAS POR FECHA ".center(50, "="))
    print("=" * 50)
    
    fecha_str = input("Ingrese fecha a buscar (YYYY-MM-DD): ")
    
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT v.id, v.fecha_venta, c.nombre, c.apellido, v.total 
                FROM ventas v
                JOIN clientes c ON v.cliente_id = c.id
                WHERE DATE(v.fecha_venta) = %s
                ORDER BY v.fecha_venta DESC
            """, (fecha,))
            ventas = cursor.fetchall()
            
            if ventas:
                print(f"\nVentas del {fecha}:")
                total_dia = 0.0
                
                for venta in ventas:
                    print(f"\nN° Venta: {venta['id']}")
                    print(f"Hora: {venta['fecha_venta'].strftime('%H:%M')}")
                    print(f"Cliente: {venta['nombre']} {venta['apellido']}")
                    print(f"Total: ${venta['total']:.2f}")
                    print("-" * 50)
                    total_dia += venta['total']
                
                print(f"\nTOTAL DEL DÍA: ${total_dia:.2f}")
            else:
                print(f"\nNo hay ventas registradas para el {fecha}.")
            
            esperar_tecla()
    except ValueError:
        print("\nFormato de fecha incorrecto. Use YYYY-MM-DD.")
        esperar_tecla()
    except Error as e:
        print(f"Error al buscar ventas: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def detalle_venta():
    limpiar_pantalla()
    print("=" * 50)
    print(" DETALLE DE VENTA ".center(50, "="))
    print("=" * 50)
    
    id_venta = input("Ingrese el número de venta: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener información general de la venta
            cursor.execute("""
                SELECT v.*, c.nombre, c.apellido 
                FROM ventas v
                JOIN clientes c ON v.cliente_id = c.id
                WHERE v.id = %s
            """, (id_venta,))
            venta = cursor.fetchone()
            
            if not venta:
                print("\nVenta no encontrada.")
                esperar_tecla()
                return
            
            print(f"\nN° Venta: {venta['id']}")
            print(f"Fecha: {venta['fecha_venta']}")
            print(f"Cliente: {venta['nombre']} {venta['apellido']}")
            print(f"Método pago: {venta['metodo_pago'].capitalize()}")
            print("\nProductos:")
            
            # Obtener detalles de la venta
            cursor.execute("""
                SELECT dv.*, p.nombre 
                FROM detalle_venta dv
                JOIN productos p ON dv.producto_id = p.id
                WHERE dv.venta_id = %s
            """, (id_venta,))
            detalles = cursor.fetchall()
            
            if detalles:
                for detalle in detalles:
                    subtotal = detalle['cantidad'] * detalle['precio_unitario']
                    print(f"- {detalle['nombre']}: {detalle['cantidad']} x ${detalle['precio_unitario']:.2f} = ${subtotal:.2f}")
            
            print(f"\nTOTAL: ${venta['total']:.2f}")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al obtener detalle: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()