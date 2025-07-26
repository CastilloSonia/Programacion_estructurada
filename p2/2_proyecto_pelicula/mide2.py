 #proyecto 1, crear un proyecto que debe gestionar (administra peliculas),
#  colocarn un menu de obsiones para agregar , borrar modificar, consultar,
# buscar y basiar peliculas , 
#notas:
#  1_ utilisar funciones y mandar llamar desde otro archivo
#  2_ utilisar diccionarios para almacenar los  siguientes atributos: (nombre, categoria, clasificacion,genero,idiomas)


import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Películas :::...\n 1.- crear  \n 2.- Borrar \n 3.- mostrar \n 4.- Agregar caracteristicas \n 5.- modificar caracteristica \n 6.- Borrar caracteristica \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").strip()

    match opcion:
        case "1":
            peliculas.CrearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            print("\n\tTerminaste la ejecución del programa.")
        case _:
            opcion=True
            input("\n\t Opción inválida. Presiona Enter para intentarlo de nuevo.")