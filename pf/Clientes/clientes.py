from funciones import *
import sys

def menu_clientes():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" GESTIÓN DE CLIENTES ".center(50, "="))
        print("=" * 50)
        print("1. Registrar nuevo cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("6. Volver al menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            esperar_tecla()

def registrar_cliente():
    limpiar_pantalla()
    print("=" * 50)
    print(" REGISTRAR NUEVO CLIENTE ".center(50, "="))
    print("=" * 50)
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO clientes (nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, email, telefono, direccion)
            cursor.execute(sql, valores)
            conexion.commit()
            print("\nCliente registrado exitosamente!")
            esperar_tecla()
    except Error as e:
        print(f"Error al registrar cliente: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def listar_clientes():
    limpiar_pantalla()
    print("=" * 50)
    print(" LISTADO DE CLIENTES ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clientes ORDER BY apellido, nombre")
            clientes = cursor.fetchall()
            
            if clientes:
                for cliente in clientes:
                    print(f"\nID: {cliente['id']}")
                    print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
                    print(f"Email: {cliente['email']}")
                    print(f"Teléfono: {cliente['telefono']}")
                    print(f"Dirección: {cliente['direccion']}")
                    print(f"Fecha Registro: {cliente['fecha_registro']}")
                    print("-" * 50)
            else:
                print("\nNo hay clientes registrados.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al listar clientes: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def buscar_cliente():
    limpiar_pantalla()
    print("=" * 50)
    print(" BUSCAR CLIENTE ".center(50, "="))
    print("=" * 50)
    
    termino = input("Ingrese nombre, apellido o email del cliente: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT * FROM clientes 
                WHERE nombre LIKE %s OR apellido LIKE %s OR email LIKE %s
                ORDER BY apellido, nombre
            """
            valores = (f"%{termino}%", f"%{termino}%", f"%{termino}%")
            cursor.execute(sql, valores)
            clientes = cursor.fetchall()
            
            if clientes:
                print("\nResultados de la búsqueda:")
                for cliente in clientes:
                    print(f"\nID: {cliente['id']}")
                    print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
                    print(f"Email: {cliente['email']}")
                    print(f"Teléfono: {cliente['telefono']}")
                    print("-" * 50)
            else:
                print("\nNo se encontraron clientes con ese criterio.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al buscar clientes: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def modificar_cliente():
    limpiar_pantalla()
    print("=" * 50)
    print(" MODIFICAR CLIENTE ".center(50, "="))
    print("=" * 50)
    
    id_cliente = input("Ingrese el ID del cliente a modificar: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            cliente = cursor.fetchone()
            
            if cliente:
                print("\nDatos actuales del cliente:")
                print(f"1. Nombre: {cliente['nombre']}")
                print(f"2. Apellido: {cliente['apellido']}")
                print(f"3. Email: {cliente['email']}")
                print(f"4. Teléfono: {cliente['telefono']}")
                print(f"5. Dirección: {cliente['direccion']}")
                print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")
                
                nombre = input(f"Nuevo nombre [{cliente['nombre']}]: ") or cliente['nombre']
                apellido = input(f"Nuevo apellido [{cliente['apellido']}]: ") or cliente['apellido']
                email = input(f"Nuevo email [{cliente['email']}]: ") or cliente['email']
                telefono = input(f"Nuevo teléfono [{cliente['telefono']}]: ") or cliente['telefono']
                direccion = input(f"Nueva dirección [{cliente['direccion']}]: ") or cliente['direccion']
                
                sql = """
                    UPDATE clientes 
                    SET nombre = %s, apellido = %s, email = %s, telefono = %s, direccion = %s 
                    WHERE id = %s
                """
                valores = (nombre, apellido, email, telefono, direccion, id_cliente)
                cursor.execute(sql, valores)
                conexion.commit()
                print("\nCliente actualizado exitosamente!")
            else:
                print("\nNo se encontró un cliente con ese ID.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al modificar cliente: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_cliente():
    limpiar_pantalla()
    print("=" * 50)
    print(" ELIMINAR CLIENTE ".center(50, "="))
    print("=" * 50)
    
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar si el cliente tiene ventas asociadas
            cursor.execute("SELECT COUNT(*) AS total FROM ventas WHERE cliente_id = %s", (id_cliente,))
            resultado = cursor.fetchone()
            
            if resultado['total'] > 0:
                print("\nNo se puede eliminar el cliente porque tiene ventas asociadas.")
                esperar_tecla()
                return
            
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            cliente = cursor.fetchone()
            
            if cliente:
                print("\nDatos del cliente a eliminar:")
                print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
                print(f"Email: {cliente['email']}")
                
                confirmacion = input("\n¿Está seguro que desea eliminar este cliente? (s/n): ").lower()
                if confirmacion == 's':
                    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
                    conexion.commit()
                    print("\nCliente eliminado exitosamente!")
                else:
                    print("\nOperación cancelada.")
            else:
                print("\nNo se encontró un cliente con ese ID.")
            
            esperar_tecla()
    except Error as e:
        print(f"Error al eliminar cliente: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()