import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n... Presione cualquier tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_agenda",
            auth_plugin='mysql_native_password'
        )
        return conexion
    except Error as e:
        print(f"\nError de conexión: {e}")
        print("Verifica que:")
        print("1. MySQL esté en ejecución")
        print("2. La base de datos 'bd_agenda' exista")
        print("3. El usuario y contraseña sean correctos")
        return None

def inicializar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conexion.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS bd_agenda")
        cursor.execute("USE bd_agenda")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                telefono VARCHAR(15) NOT NULL,
                email VARCHAR(50),
                direccion VARCHAR(100),
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conexion.commit()
        print("\nBase de datos inicializada correctamente")
    except Error as e:
        print(f"\nError al inicializar BD: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def agregar_contacto():
    borrarPantalla()
    print("\n.:: Agregar Nuevo Contacto ::.\n")
    
    contacto = {
        "nombre": input("Nombre: ").title().strip(),
        "telefono": input("Teléfono: ").strip(),
        "email": input("Email (opcional): ").strip() or None,
        "direccion": input("Dirección (opcional): ").strip() or None
    }
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO contactos 
                    (nombre, telefono, email, direccion) 
                    VALUES (%s, %s, %s, %s)"""
            valores = (
                contacto["nombre"],
                contacto["telefono"],
                contacto["email"],
                contacto["direccion"]
            )
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n::: Contacto agregado con éxito :::")
        except Error as e:
            print(f"\nError al agregar contacto: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def mostrar_contactos():
    borrarPantalla()
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM contactos ORDER BY nombre")
            contactos = cursor.fetchall()
            
            if contactos:
                print("\n.:: Listado de Contactos ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<20}{'TELÉFONO':<15}{'EMAIL':<25}{'DIRECCIÓN':<20}")
                print("-"*85)
                for contacto in contactos:
                    print(f"{contacto['id']:<5}{contacto['nombre']:<20}{contacto['telefono']:<15}" +
                          f"{contacto['email'] or 'N/A':<25}{contacto['direccion'] or 'N/A':<20}")
                print("-"*85)
            else:
                print("\nNo hay contactos registrados")
        except Error as e:
            print(f"\nError al obtener contactos: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def buscar_contacto():
    borrarPantalla()
    termino = input("\nIngrese nombre o teléfono a buscar: ").strip()
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """SELECT * FROM contactos 
                    WHERE nombre LIKE %s OR telefono LIKE %s 
                    ORDER BY nombre"""
            val = (f"%{termino}%", f"%{termino}%")
            cursor.execute(sql, val)
            contactos = cursor.fetchall()
            
            if contactos:
                print("\n.:: Resultados de Búsqueda ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<20}{'TELÉFONO':<15}{'EMAIL':<25}")
                print("-"*65)
                for contacto in contactos:
                    print(f"{contacto['id']:<5}{contacto['nombre']:<20}" +
                          f"{contacto['telefono']:<15}{contacto['email'] or 'N/A':<25}")
                print("-"*65)
            else:
                print("\nNo se encontraron contactos con ese criterio")
        except Error as e:
            print(f"\nError al buscar contactos: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def modificar_contacto():
    borrarPantalla()
    mostrar_contactos()
    id_contacto = input("\nIngrese el ID del contacto a modificar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM contactos WHERE id = %s", (id_contacto,))
            contacto = cursor.fetchone()
            
            if contacto:
                print("\nDatos actuales del contacto:")
                print(f"1. Nombre: {contacto['nombre']}")
                print(f"2. Teléfono: {contacto['telefono']}")
                print(f"3. Email: {contacto['email'] or 'N/A'}")
                print(f"4. Dirección: {contacto['direccion'] or 'N/A'}")
                
                print("\nIngrese los nuevos datos (deje en blanco para no modificar):")
                nuevos_datos = {
                    "nombre": input("Nuevo nombre: ").title().strip() or contacto['nombre'],
                    "telefono": input("Nuevo teléfono: ").strip() or contacto['telefono'],
                    "email": input("Nuevo email: ").strip() or contacto['email'],
                    "direccion": input("Nueva dirección: ").strip() or contacto['direccion']
                }
                
                confirmacion = input("\n¿Confirmar cambios? (S/N): ").upper()
                if confirmacion == "S":
                    cursor.execute("""
                        UPDATE contactos SET 
                        nombre = %s, 
                        telefono = %s, 
                        email = %s, 
                        direccion = %s 
                        WHERE id = %s
                    """, (
                        nuevos_datos['nombre'],
                        nuevos_datos['telefono'],
                        nuevos_datos['email'],
                        nuevos_datos['direccion'],
                        id_contacto
                    ))
                    conexion.commit()
                    print("\n::: Contacto actualizado con éxito :::")
            else:
                print("\nNo se encontró un contacto con ese ID")
        except Error as e:
            print(f"\nError al modificar contacto: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def borrar_contacto():
    borrarPantalla()
    mostrar_contactos()
    id_contacto = input("\nIngrese el ID del contacto a eliminar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM contactos WHERE id = %s", (id_contacto,))
            contacto = cursor.fetchone()
            
            if contacto:
                print("\nDatos del contacto a eliminar:")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                
                confirmacion = input("\n¿Está seguro de eliminar este contacto? (S/N): ").upper()
                if confirmacion == "S":
                    cursor.execute("DELETE FROM contactos WHERE id = %s", (id_contacto,))
                    conexion.commit()
                    print("\n::: Contacto eliminado con éxito :::")
            else:
                print("\nNo se encontró un contacto con ese ID")
        except Error as e:
            print(f"\nError al eliminar contacto: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def menu_principal():
    print("\n.:: AGENDA DE CONTACTOS ::.")
    print("\n1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Eliminar contacto")
    print("6. Inicializar/Verificar base de datos")
    print("7. Salir")
    return input("\nSeleccione una opción: ")