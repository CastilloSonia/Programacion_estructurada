import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t... Presione cualquier tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def agregar_calificaciones():
    borrarPantalla()
    print("\n\t\t.:: Agregar Alumno y Calificaciones ::.\n")
    
    alumno = {
        "nombre": input("Ingresa el nombre del alumno: ").title().strip(),
        "calif1": float(input("Ingresa la calificación 1: ")),
        "calif2": float(input("Ingresa la calificación 2: ")),
        "calif3": float(input("Ingresa la calificación 3: "))
    }
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO alumnos 
                    (nombre, calificacion1, calificacion2, calificacion3) 
                    VALUES (%s, %s, %s, %s)"""
            valores = (
                alumno["nombre"], 
                alumno["calif1"],
                alumno["calif2"],
                alumno["calif3"]
            )
            cursor.execute(sql, valores)
            conexion.commit()
            print("\n\t::: Datos del alumno registrados con éxito :::")
        except Error as e:
            print(f"\n\tError al registrar alumno: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def mostrar_calificaciones():
    borrarPantalla()
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos")
            alumnos = cursor.fetchall()
            
            if alumnos:
                print("\n\t\t.:: Listado de Alumnos y Calificaciones ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
                print("-"*65)
                for alumno in alumnos:
                    promedio = (alumno['calificacion1'] + alumno['calificacion2'] + alumno['calificacion3']) / 3
                    print(f"{alumno['id']:<5}{alumno['nombre']:<20}{alumno['calificacion1']:<10.1f}{alumno['calificacion2']:<10.1f}{alumno['calificacion3']:<10.1f}{promedio:<10.1f}")
                print("-"*65)
            else:
                print("\n\tNo hay alumnos registrados")
        except Error as e:
            print(f"\n\tError al obtener datos: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def calcular_promedios():
    borrarPantalla()
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT nombre, calificacion1, calificacion2, calificacion3 FROM alumnos")
            alumnos = cursor.fetchall()
            
            if alumnos:
                print("\n\t\t.:: Promedios de Alumnos ::.\n")
                print(f"{'NOMBRE':<20}{'PROMEDIO':<10}{'ESTADO':<15}")
                print("-"*45)
                for alumno in alumnos:
                    promedio = (alumno['calificacion1'] + alumno['calificacion2'] + alumno['calificacion3']) / 3
                    estado = "APROBADO" if promedio >= 6.0 else "REPROBADO"
                    print(f"{alumno['nombre']:<20}{promedio:<10.1f}{estado:<15}")
                print("-"*45)
                
                # Calcular promedio general
                cursor.execute("SELECT AVG((calificacion1 + calificacion2 + calificacion3)/3) as promedio_general FROM alumnos")
                promedio_general = cursor.fetchone()['promedio_general']
                print(f"\n\tPromedio general del grupo: {promedio_general:.1f}")
            else:
                print("\n\tNo hay alumnos registrados")
        except Error as e:
            print(f"\n\tError al calcular promedios: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def buscar_alumno():
    borrarPantalla()
    nombre = input("\nIngrese el nombre del alumno a buscar: ").title().strip()
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos WHERE nombre LIKE %s", (f"%{nombre}%",))
            alumnos = cursor.fetchall()
            
            if alumnos:
                print("\n\t\t.:: Resultados de Búsqueda ::.\n")
                print(f"{'ID':<5}{'NOMBRE':<20}{'CALIF1':<10}{'CALIF2':<10}{'CALIF3':<10}{'PROMEDIO':<10}")
                print("-"*65)
                for alumno in alumnos:
                    promedio = (alumno['calificacion1'] + alumno['calificacion2'] + alumno['calificacion3']) / 3
                    print(f"{alumno['id']:<5}{alumno['nombre']:<20}{alumno['calificacion1']:<10.1f}{alumno['calificacion2']:<10.1f}{alumno['calificacion3']:<10.1f}{promedio:<10.1f}")
                print("-"*65)
            else:
                print("\n\tNo se encontraron alumnos con ese nombre")
        except Error as e:
            print(f"\n\tError al buscar alumno: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def modificar_calificaciones():
    borrarPantalla()
    mostrar_calificaciones()
    id_alumno = input("\nIngrese el ID del alumno a modificar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id_alumno,))
            alumno = cursor.fetchone()
            
            if alumno:
                print("\nDatos actuales del alumno:")
                print(f"Nombre: {alumno['nombre']}")
                print(f"Calificación 1: {alumno['calificacion1']}")
                print(f"Calificación 2: {alumno['calificacion2']}")
                print(f"Calificación 3: {alumno['calificacion3']}")
                
                print("\nIngrese los nuevos datos (deje en blanco para no modificar):")
                nuevos_datos = {
                    "nombre": input("Nuevo nombre: ").title().strip() or alumno['nombre'],
                    "calif1": input("Nueva calificación 1: ") or alumno['calificacion1'],
                    "calif2": input("Nueva calificación 2: ") or alumno['calificacion2'],
                    "calif3": input("Nueva calificación 3: ") or alumno['calificacion3']
                }
                
                # Convertir calificaciones a float
                try:
                    nuevos_datos["calif1"] = float(nuevos_datos["calif1"])
                    nuevos_datos["calif2"] = float(nuevos_datos["calif2"])
                    nuevos_datos["calif3"] = float(nuevos_datos["calif3"])
                except ValueError:
                    print("\n\tError: Las calificaciones deben ser números")
                    return
                
                confirmacion = input("\n¿Confirmar cambios? (S/N): ").upper()
                if confirmacion == "S":
                    cursor.execute("""
                        UPDATE alumnos SET 
                        nombre = %s, 
                        calificacion1 = %s, 
                        calificacion2 = %s, 
                        calificacion3 = %s 
                        WHERE id = %s
                    """, (
                        nuevos_datos['nombre'],
                        nuevos_datos['calif1'],
                        nuevos_datos['calif2'],
                        nuevos_datos['calif3'],
                        id_alumno
                    ))
                    conexion.commit()
                    print("\n\t::: Calificaciones actualizadas con éxito :::")
            else:
                print("\n\tNo se encontró un alumno con ese ID")
        except Error as e:
            print(f"\n\tError al modificar calificaciones: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def eliminar_alumno():
    borrarPantalla()
    mostrar_calificaciones()
    id_alumno = input("\nIngrese el ID del alumno a eliminar: ")
    
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id_alumno,))
            alumno = cursor.fetchone()
            
            if alumno:
                print("\nDatos del alumno a eliminar:")
                print(f"Nombre: {alumno['nombre']}")
                print(f"Calificaciones: {alumno['calificacion1']}, {alumno['calificacion2']}, {alumno['calificacion3']}")
                
                confirmacion = input("\n¿Está seguro de eliminar este alumno? (S/N): ").upper()
                if confirmacion == "S":
                    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_alumno,))
                    conexion.commit()
                    print("\n\t::: Alumno eliminado con éxito :::")
            else:
                print("\n\tNo se encontró un alumno con ese ID")
        except Error as e:
            print(f"\n\tError al eliminar alumno: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def menu_principal():
    print("\n\t\t.:: SISTEMA DE GESTIÓN DE CALIFICACIONES ::.")
    print("\n\t1. Agregar alumno y calificaciones")
    print("\t2. Mostrar todos los alumnos")
    print("\t3. Calcular promedios")
    print("\t4. Buscar alumno")
    print("\t5. Modificar calificaciones")
    print("\t6. Eliminar alumno")
    print("\t7. Salir")
    return input("\n\tSeleccione una opción: ")