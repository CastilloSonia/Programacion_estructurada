#proyecto 1, crear un proyecto que debe gestionar (administra peliculas),
#  colocar un menu de opciones para agregar , borrar modificar, consultar,
# buscar y vaciar películas , 
# notas:
#  1_ utilizar funciones y mandar llamar desde otro archivo
#  2_ utilizar diccionarios para almacenar los  siguientes atributos: (nombre, categoria, clasificacion,genero,idiomas)


import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Películas :::...\n 1.- Crear  \n 2.- Mostrar \n 3.- Buscar \n 4.- Borrar \n 5.- Modificar \n 6.- SALIR ")
    opcion = input("\t Elige una opción: ").strip()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion = False
            print("\n\tTerminaste la ejecución del programa.")
        case _:
            opcion=True
            input("\n\t Opción inválida. Presiona Enter para intentarlo de nuevo.")