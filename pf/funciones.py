import os
import sys
import mysql.connector
from mysql.connector import Error
import getpass  # Para ocultar la contraseña al escribirla
from datetime import datetime

def limpiar_pantalla():
    """🧹 Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    """⌨️ Espera que el usuario presione una tecla para continuar"""
    input("\n🔘 Presione cualquier tecla para continuar...")

def conectar_bd():
    """🔌 Establece conexión con la base de datos MySQL"""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tienda_ropa'
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

def crear_tablas():
    """🛠️ Crea las tablas necesarias en la base de datos si no existen"""
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            
            # Tabla Clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL,
                    apellido VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    telefono VARCHAR(20),
                    direccion VARCHAR(100),
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabla Productos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT,
                    categoria ENUM('camisas', 'pantalones', 'vestidos', 'zapatos', 'accesorios') NOT NULL,
                    talla ENUM('XS', 'S', 'M', 'L', 'XL', 'XXL', 'Única') NOT NULL,
                    color VARCHAR(30) NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL,
                    stock INT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabla Ventas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ventas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente_id INT NOT NULL,
                    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total DECIMAL(10, 2) NOT NULL,
                    metodo_pago ENUM('efectivo', 'tarjeta', 'transferencia') NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                )
            """)
            
            # Tabla Detalle_Venta
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS detalle_venta (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    venta_id INT NOT NULL,
                    producto_id INT NOT NULL,
                    cantidad INT NOT NULL,
                    precio_unitario DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (venta_id) REFERENCES ventas(id),
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                )
            """)
            
            # Tabla Inventario
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventario (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    producto_id INT NOT NULL,
                    tipo ENUM('entrada', 'salida', 'ajuste') NOT NULL,
                    cantidad INT NOT NULL,
                    motivo VARCHAR(100) NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    usuario VARCHAR(50) NOT NULL,
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                )
            """)
            
            conexion.commit()
            cursor.close()
            conexion.close()
            
    except Error as e:
        print(f"❌ Error al crear tablas: {e}")

def crear_tabla_usuarios():
    """👤 Crea la tabla de usuarios si no existe"""
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    nombre VARCHAR(100) NOT NULL,
                    rol ENUM('admin', 'vendedor') DEFAULT 'vendedor',
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conexion.commit()
            
            # Crear usuario admin por defecto si no existe
            cursor.execute("SELECT * FROM usuarios WHERE username = 'admin'")
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO usuarios (username, password, nombre, rol)
                    VALUES ('admin', 'admin123', 'Administrador', 'admin')
                """)
                conexion.commit()
            
            cursor.close()
            conexion.close()
    except Error as e:
        print(f"❌ Error al crear tabla usuarios: {e}")

def registrar_usuario():
    """📝 Registra un nuevo usuario en el sistema"""
    limpiar_pantalla()
    print("=" * 50)
    print(" 📝 REGISTRO DE USUARIO ".center(50, "="))
    print("=" * 50)
    
    username = input("👤 Nombre de usuario: ")
    password = getpass.getpass("🔒 Contraseña: ")
    confirm_password = getpass.getpass("🔏 Confirmar contraseña: ")
    nombre = input("🏷️ Nombre completo: ")
    
    if password != confirm_password:
        print("\n❌ Las contraseñas no coinciden")
        esperar_tecla()
        return False
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (username, password, nombre) VALUES (%s, %s, %s)"
            valores = (username, password, nombre)
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n✅ Usuario registrado exitosamente!")
            esperar_tecla()
            return True
    except Error as e:
        print(f"\n❌ Error al registrar usuario: {e}")
        esperar_tecla()
        return False
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def iniciar_sesion():
    """🔑 Autentica a un usuario en el sistema"""
    intentos = 3
    while intentos > 0:
        limpiar_pantalla()
        print("=" * 50)
        print(" 🔐 INICIO DE SESIÓN ".center(50, "="))
        print("=" * 50)
        
        username = input("👤 Usuario: ")
        password = getpass.getpass("🔒 Contraseña: ")
        
        try:
            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor(dictionary=True)
                sql = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
                cursor.execute(sql, (username, password))
                usuario = cursor.fetchone()
                
                if usuario:
                    print(f"\n🎉 ¡Bienvenido(a), {usuario['nombre']}!")
                    esperar_tecla()
                    return usuario
                else:
                    intentos -= 1
                    print(f"\n⚠️ Credenciales incorrectas. Intentos restantes: {intentos}")
                    esperar_tecla()
        except Error as e:
            print(f"\n❌ Error al iniciar sesión: {e}")
            esperar_tecla()
        finally:
            if 'conexion' in locals() and conexion.is_connected():
                cursor.close()
                conexion.close()
    
    print("\n🚫 Has excedido el número máximo de intentos. Saliendo...")
    return None

# ========================================================
# FUNCIONES ORIGINALES DEL SISTEMA (CON EMOJIS AÑADIDOS)
# ========================================================

def registrar_cliente():
    """📝 Registra un nuevo cliente"""
    limpiar_pantalla()
    print("=" * 50)
    print(" 📝 REGISTRAR NUEVO CLIENTE ".center(50, "="))
    print("=" * 50)
    
    nombre = input("👤 Nombre: ")
    apellido = input("👥 Apellido: ")
    email = input("📧 Email: ")
    telefono = input("📱 Teléfono: ")
    direccion = input("🏠 Dirección: ")
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO clientes (nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, email, telefono, direccion)
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n✅ Cliente registrado exitosamente!")
            esperar_tecla()
    except Error as e:
        print(f"❌ Error al registrar cliente: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def listar_clientes():
    """📋 Lista todos los clientes"""
    limpiar_pantalla()
    print("=" * 50)
    print(" 📋 LISTADO DE CLIENTES ".center(50, "="))
    print("=" * 50)
    
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clientes ORDER BY apellido, nombre")
            clientes = cursor.fetchall()
            
            if clientes:
                for cliente in clientes:
                    print(f"\n🆔 ID: {cliente['id']}")
                    print(f"👤 Nombre: {cliente['nombre']} {cliente['apellido']}")
                    print(f"📧 Email: {cliente['email']}")
                    print(f"📱 Teléfono: {cliente['telefono']}")
                    print(f"🏠 Dirección: {cliente['direccion']}")
                    print(f"📅 Fecha Registro: {cliente['fecha_registro']}")
                    print("-" * 50)
            else:
                print("\nℹ️ No hay clientes registrados.")
            
            esperar_tecla()
    except Error as e:
        print(f"❌ Error al listar clientes: {e}")
        esperar_tecla()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

# ... (aquí irían todas las demás funciones originales del sistema, 
# cada una con sus emojis correspondientes pero con la misma funcionalidad original) ...