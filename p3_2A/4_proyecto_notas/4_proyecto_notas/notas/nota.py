from conexionBD import *


def crar(usuario_id, titulo, descripcion):
    try:
        cursor.execute("insert into notas(usuareio_id, titulo, descripcion, fecha) value(%s, %s, %s, NOW())", (usuario_id, titulo, descripcion))
        conexion.commit
        return True
    except:
        return False 
    
def mostrar(usuario_id):
    try:
        cursor.execuute("select * from notasn where usuario_id=%s",(usuario_id))
        lista=cursor.fetchall()
        if len(lista)>0: 
            return lista
        else:
            return[]
    except:
        return []
def cambiar(id, titulo, descripcion):
    try: 
        cursor.execute("update notas ser tiulo=%s,descripcion=%s, fecha=NOW() where id=%s", (titulo, descripcion, id))
        conexion.commit()
        return True
    except:
        return False 
def borrar(id):
    try:
        cursor.execute("delete from  nottas where id=%s", (id))
        conexion.commit()
        return True
    except:
        return False
