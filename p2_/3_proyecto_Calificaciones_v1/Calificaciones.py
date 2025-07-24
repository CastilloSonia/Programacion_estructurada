# listas[
#         ["Ruben", 10.0, 10.0 , 10.0],
#         ["Diana", 10.0, 9.8 , 8.0],
#         ["Jose", 5.0, 6.0, 7.o]
# ]

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("Oprima cualquier tecla para continuar ...")
    
def menu_principal():
     print("\n\t\t\t..::: Sistema de Gestión de Calificaciones :::...\n 1.- Agregar  \n 2.- Mostrar \n 3.- Calcular Promedio \n 4.- SALIR ")
     opcion = input("\t Elige una opción: ").strip()
     return opcion
    
def agregar_Calificaciones(lista):
    nombre = input("\n\t Ingrese el nombre del alumno: ").strip()
    calificacion1 = float(input("\t Ingrese la primera calificación: "))
    calificacion2 = float(input("\t Ingrese la segunda calificación: "))
    calificacion3 = float(input("\t Ingrese la tercera calificación: "))
    
    calificaciones.append([nombre, calificacion1, calificacion2, calificacion3])
    print(f"\n\t Calificaciones de {nombre} agregadas correctamente.")
    def mostrar_Calificaciones(lista):