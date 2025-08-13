from funciones import *

def menu_inventario():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" GESTIÓN DE INVENTARIO ".center(50, "="))
        print("=" * 50)
        print("1. Listar productos")
        print("2. Registrar nuevo producto")
        print("3. Actualizar stock")
        print("4. Movimientos de inventario")
        print("5. Volver al menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            registrar_producto()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            movimientos_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            esperar_tecla()

def listar_productos():
    limpiar_pantalla()
    print("=" * 50)
    print(" LISTADO DE PRODUCTOS ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT p.*, 
                    (SELECT SUM(cantidad) FROM inventario 
                    WHERE producto_id = p.id AND tipo = 'entrada') AS entradas,
                    (SELECT SUM(cantidad) FROM inventario 
                    WHERE producto_id = p.id AND tipo = 'salida') AS salidas
                FROM productos p
                ORDER BY p.nombre
            """)
            productos = cursor.fetchall()
            
            if productos:
                for producto in productos:
                    stock_actual = producto['stock']
                    entradas = producto['entradas'] or 0
                    salidas = producto['salidas'] or 0
                    
                    print(f"\nID: {producto['id']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Categoría: {producto['categoria'].capitalize()}")
                    print(f"Talla: {producto['talla']}")
                    print(f"Color: {producto['color']}")
                    print(f"Precio: ${producto['precio']:.2f}")
                    print(f"Stock actual: {stock_actual}")
                    print(f"Entradas totales: {entradas}")
                    print(f"Salidas totales: {salidas}")
                    print("-" * 50)
            else:
                print("\nNo hay productos registrados.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al listar productos: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def registrar_producto():
    limpiar_pantalla()
    print("=" * 50)
    print(" REGISTRAR NUEVO PRODUCTO ".center(50, "="))
    print("=" * 50)
    
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    
    print("\nCategorías disponibles:")
    print("1. Camisas")
    print("2. Pantalones")
    print("3. Vestidos")
    print("4. Zapatos")
    print("5. Accesorios")
    opcion_cat = input("Seleccione categoría (1-5): ")
    categorias = {1: 'camisas', 2: 'pantalones', 3: 'vestidos', 4: 'zapatos', 5: 'accesorios'}
    categoria = categorias.get(int(opcion_cat), 'camisas')
    
    print("\nTallas disponibles:")
    print("1. XS")
    print("2. S")
    print("3. M")
    print("4. L")
    print("5. XL")
    print("6. XXL")
    print("7. Única")
    opcion_talla = input("Seleccione talla (1-7): ")
    tallas = {1: 'XS', 2: 'S', 3: 'M', 4: 'L', 5: 'XL', 6: 'XXL', 7: 'Única'}
    talla = tallas.get(int(opcion_talla), 'M')
    
    color = input("Color: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO productos 
                (nombre, descripcion, categoria, talla, color, precio, stock) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, descripcion, categoria, talla, color, precio, stock)
            cursor.execute(sql, valores)
            
            # Registrar movimiento de inventario
            producto_id = cursor.lastrowid
            sql_movimiento = """
                INSERT INTO inventario 
                (producto_id, tipo, cantidad, motivo, usuario) 
                VALUES (%s, 'entrada', %s, 'Stock inicial', 'sistema')
            """
            cursor.execute(sql_movimiento, (producto_id, stock))
            
            conexion.commit()
            print("\nProducto registrado exitosamente!")
            esperar_tecla()
    except Error as e:
        print(f"Error al registrar producto: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def actualizar_stock():
    limpiar_pantalla()
    print("=" * 50)
    print(" ACTUALIZAR STOCK DE PRODUCTO ".center(50, "="))
    print("=" * 50)
    
    id_producto = input("Ingrese el ID del producto: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos WHERE id = %s", (id_producto,))
            producto = cursor.fetchone()
            
            if producto:
                print("\nDatos del producto:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Stock actual: {producto['stock']}")
                print("\nTipos de movimiento:")
                print("1. Entrada (aumentar stock)")
                print("2. Salida (reducir stock)")
                print("3. Ajuste (establecer nuevo valor)")
                
                opcion = input("\nSeleccione tipo de movimiento (1-3): ")
                tipos = {1: 'entrada', 2: 'salida', 3: 'ajuste'}
                tipo = tipos.get(int(opcion), 'ajuste')
                
                if tipo == 'entrada':
                    cantidad = int(input("Cantidad a ingresar: "))
                    nuevo_stock = producto['stock'] + cantidad
                elif tipo == 'salida':
                    cantidad = int(input("Cantidad a sacar: "))
                    if cantidad > producto['stock']:
                        print("\nNo hay suficiente stock disponible.")
                        esperar_tecla()
                        return
                    nuevo_stock = producto['stock'] - cantidad
                else:  # ajuste
                    nuevo_stock = int(input("Nuevo valor de stock: "))
                    cantidad = abs(nuevo_stock - producto['stock'])
                
                motivo = input("Motivo del movimiento: ")
                
                # Actualizar stock del producto
                cursor.execute("UPDATE productos SET stock = %s WHERE id = %s", (nuevo_stock, id_producto))
                
                # Registrar movimiento de inventario
                sql_movimiento = """
                    INSERT INTO inventario 
                    (producto_id, tipo, cantidad, motivo, usuario) 
                    VALUES (%s, %s, %s, %s, 'admin')
                """
                cursor.execute(sql_movimiento, (id_producto, tipo, cantidad, motivo))
                
                conexion.commit()
                print("\nStock actualizado exitosamente!")
            else:
                print("\nNo se encontró un producto con ese ID.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al actualizar stock: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def movimientos_inventario():
    limpiar_pantalla()
    print("=" * 50)
    print(" MOVIMIENTOS DE INVENTARIO ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT i.*, p.nombre AS producto 
                FROM inventario i
                JOIN productos p ON i.producto_id = p.id
                ORDER BY i.fecha DESC
                LIMIT 50
            """)
            movimientos = cursor.fetchall()
            
            if movimientos:
                for mov in movimientos:
                    print(f"\nID: {mov['id']}")
                    print(f"Producto: {mov['producto']} (ID: {mov['producto_id']})")
                    print(f"Tipo: {mov['tipo'].capitalize()}")
                    print(f"Cantidad: {mov['cantidad']}")
                    print(f"Motivo: {mov['motivo']}")
                    print(f"Usuario: {mov['usuario']}")
                    print(f"Fecha: {mov['fecha']}")
                    print("-" * 50)
            else:
                print("\nNo hay movimientos registrados.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al obtener movimientos: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()