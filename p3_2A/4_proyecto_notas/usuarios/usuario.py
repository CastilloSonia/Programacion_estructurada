from conexionBD import *
import datetime
import hashlib

def hash_passwor(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellido,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrsena=hash_passwor(contrasena)
        sql=" insert into usuarios(nombre,apellido,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=()
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contrasena):
    try:
        contrsena=hash_passwor(contrasena)
        sql="select * from usuario where email=%s and password=%s"
        val=()
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
    