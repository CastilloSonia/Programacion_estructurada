from calificaciones import *

def main():
    while True:
        borrarPantalla()
        opcion = menu_principal()
        
        if opcion == "1":
            agregar_calificaciones()
            esperarTecla()
        elif opcion == "2":
            mostrar_calificaciones()
            esperarTecla()
        elif opcion == "3":
            calcular_promedios()
            esperarTecla()
        elif opcion == "4":
            buscar_alumno()
            esperarTecla()
        elif opcion == "5":
            modificar_calificaciones()
            esperarTecla()
        elif opcion == "6":
            eliminar_alumno()
            esperarTecla()
        elif opcion == "7":
            print("\n\tSaliendo del sistema...")
            break
        else:
            print("\n\tOpción no válida, intente nuevamente")
            esperarTecla()

if __name__ == "__main__":
    main()