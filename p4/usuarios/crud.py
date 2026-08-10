def insertar(nombre, correo, rol, estudiante, conexionBD):
    try:
        if conexionBD != None:
            cursor=conexionBD.cursor()
            cursor.execute("insert into usuarios values (null,%s,%s,%s,%s)", (nombre, correo, rol, estudiante))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False
    
def consultar(conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor(dictionary=True)
            cursor.execute("select * from usuarios")
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            
            # 1. Borramos la tabla y reiniciamos el contador AUTO_INCREMENT
            cursor.execute("TRUNCATE TABLE usuarios")
            
            # 2. Re-insertamos automáticamente al Administrador por defecto (ID será 1)
            sql_admin = """
                INSERT INTO usuarios (id, nombre, correo, rol, estudiante)
                VALUES (NULL, 'ADMINISTRADOR GENERAL', 'admin@gmail.com', 'EMPLEADO', 'NO')
            """
            cursor.execute(sql_admin)
            
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False

def buscar_por_correo(correo, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor(dictionary=True)
            cursor.execute("select * from usuarios where correo=%s", (correo,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def buscar_por_nombre(nombre, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor(dictionary=True)
            #Agregaremos like para buscar y encontrar coinsidencias
            sql = "select * from usuarios where nombre like %s"
            patron = f"%{nombre}%"

            cursor.execute(sql, (patron,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def buscar_por_rol(rol, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor(dictionary=True)
            cursor.execute("select * from usuarios where rol=%s", (rol,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def borrar(id_usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False
    
def actualizar(nombre_new, correo, rol, estudiante, nombre_old, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "UPDATE usuarios SET nombre=%s, correo=%s, rol=%s, estudiante=%s WHERE nombre=%s"
            cursor.execute(sql, (nombre_new, correo, rol, estudiante, nombre_old))
            conexionBD.commit()
            
            # 📌 Verificamos que realmente se haya modificado al menos 1 fila en MySQL
            if cursor.rowcount > 0:
                return True
            else:
                print("\n[!] No se encontró ninguna coincidencia exacta para actualizar.")
                return False
        else:
            return False
    except Exception as e:
        print(f"Error en BD: {e}")
        return False