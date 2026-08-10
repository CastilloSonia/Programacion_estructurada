def insertar(id_usuario, id_libro, fecha_renta, fecha_devolucion, estado, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("insert into rentas values (null,%s,%s,%s,%s,%s)", (id_usuario, id_libro, fecha_renta, fecha_devolucion, estado))
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
            cursor.execute("select * from rentas")
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def buscar_id_usuario(id_usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select r.id, r.id_libro, l.titulo, r.fecha_renta, r.fecha_devolucion, r.estado from rentas r inner join libros l on r.id_libro = l.id where r.id_usuario=%s order by r.id desc", (id_usuario,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def buscar_activas_por_usuario(id_usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select r.id, r.id_libro, l.titulo, r.fecha_renta, r.fecha_devolucion, r.estado from rentas r inner join libros l on r.id_libro = l.id where r.id_usuario=%s and r.estado='ACTIVA' order by r.id desc", (id_usuario,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def consultar_todas_activas(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select r.id, u.nombre as cliente, l.id as id_libro, l.titulo as libro, r.fecha_renta, r.fecha_devolucion, r.estado from rentas r inner join usuarios u on r.id_usuario = u.id inner join libros l on r.id_libro = l.id where r.estado='ACTIVA' order by r.id desc")
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def consultar_historial_general(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor(dictionary=True)
            cursor.execute("select r.id, u.nombre as cliente, l.titulo as libro, r.fecha_renta, r.fecha_devolucion, r.estado from rentas r inner join usuarios u on r.id_usuario = u.id inner join libros l on r.id_libro = l.id order by r.id desc")
            return cursor.fetchall()
        else:
            return []
    except:
        return []


def actualizar_estado(id_renta, nuevo_estado, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update rentas set estado=%s where id=%s", (nuevo_estado, id_renta))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False


def borrar(id_renta, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from rentas where id=%s", (id_renta,))
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
            cursor.execute("truncate rentas")
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False