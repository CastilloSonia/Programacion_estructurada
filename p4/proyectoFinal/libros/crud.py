def insertar(titulo, autor, categoria, stock, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("insert into libros values (null,%s,%s,%s,%s)", (titulo, autor, categoria, stock))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False


def consultar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select * from libros")
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def buscar_por_id(id_libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select * from libros where id=%s", (id_libro,))
            return cursor.fetchone()
        else:
            return None
    except:
        return None


def buscar_por_titulo(titulo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            sql = "select * from libros where titulo like %s"
            patron = f"%{titulo}%"
            cursor.execute(sql, (patron,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def buscar_por_autor(autor, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select * from libros where autor=%s", (autor,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def buscar_por_categoria(categoria, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select * from libros where categoria=%s", (categoria,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def borrar(id_libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from libros where id=%s", (id_libro,))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False


def actualizar(titulo_new, autor, categoria, stock, id_libro, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update libros set titulo=%s, autor=%s, categoria=%s, stock=%s where id=%s", (titulo_new, autor, categoria, stock, id_libro))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False


def actualizar_stock(id_libro, nuevo_stock, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update libros set stock=%s where id=%s", (nuevo_stock, id_libro))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False


def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("truncate libros")
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False