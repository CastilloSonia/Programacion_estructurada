
# Proyecto 1, crear un proyecto que debe gestionar (administra peliculas),
#  colocar un menu de opciones para agregar , 
# modificar, consultar,
# buscar y vaciar peliculas , 
#notas: 1_ utilizar funciones y mandar llamar desde otro archivo
#  2_ utilizar una lista para almacenar los nombres de las peliculas 
import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Películas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").strip()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            print("\n\tTerminaste la ejecución del programa.")
        case _:
            opcion=True
            input("\n\t Opción inválida. Presiona Enter para intentarlo de nuevo.")
            