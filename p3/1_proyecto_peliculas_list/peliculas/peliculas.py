import funciones
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Ingresa la pelicula: ").upper().strip()
    pelis.append(peli)
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR PELICULAS ::::...\n")
    print("\tCódigo\t\tPelícula")
    for i in range(0,len(pelis)):
        print(f"\t{i+1}\t\t{pelis[i]}")
    funciones.espereTecla()
   
def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS PELICULAS ::::...\n") 
     if len(pelis)>0:
         opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         if opc=="si":
             pelis=pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen peliculas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        print("\tCódigo\t\tPelícula")
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
              print(f"\t{i+1}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\t...¡No existe la pelicula que andas buscando!...")

def borrarPeliculas(pelis):
    posiciones=[]
    print("\t\t....:::: BORRAR PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
              opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
              while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
              if opc=="si":
                posiciones.append(i)
        if len(posiciones)>0:
            for i in range(0,len(posiciones)):
                pelis.remove(peli)
        funciones.accionExitosa()
    else:
        input("\n\t...¡No existe la pelicula que andas buscando!...")

def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
              opc=input("¿Deseas mofificar la pelicula (Si/No)? ").lower().strip()
              while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la pelicula (Si/No)? ").lower().strip()
              if opc=="si":
                pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                funciones.accionExitosa()
    else:
        input("\n\t...¡No existe la pelicula que andas buscando!...")
 


