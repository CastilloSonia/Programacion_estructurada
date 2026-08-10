import mysql.connector

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="biblioteca_bd"
        )
        print("..::: Conexion exitosa :::..")
        return conexion
        
    except ValueError as e:
        print(f"Error de conexion {e}")
        input("...Por el momento no es posible establecer conexion con la base de datos intentelo mas tardr...")
        return None
