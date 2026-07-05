import funciones
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR CARACTERISTICAS A UNA PELICULA ::::...\n")
    caracterisitica=input("Ingresa la Caracteristica: ").lower().strip()
    valor=input("Ingresa el valor de la Catracteristica: ").upper().strip()
    pelis[caracterisitica]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis) > 0:
        print("\tCaracteristica \t\tValor")
        for i in pelis:
            print(f"\t{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("....No existe ninguna caracteristica en la pelicula, verifique!....")
    
def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS LAS CARACTERISTCAS ::::...\n") 
     if len(pelis)>0:
         opc=""
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las caracteristicas de la pelicula? (Si/No): ").lower().strip()
         if opc=="si":
             pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen peliculas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR CARACTERISTICAS DE LA PELICULA ::::...\n")   
    caracteristica=input("Escribe el nombre LA caracteristica: ").upper().strip()
    print("\tCaracteristica\t\tValor")  
    noencontro=False
    for i in pelis:
        if caracteristica == i:
            print(f"\t{i}\t\t{pelis[i]}")
            noencontro = True
        funciones.espereTecla()
    if not(noencontro):
        input("\n\t...¡No existe esta caracteristica que andas buscando!...")

def borrarPeliculas(pelis):
    posiciones=[]
    print("\t\t....:::: BORRAR  CARACTERISTICA ::::...\n")   
    caracteristica=input("Escribe el nombre de la caracteristica: ").upper().strip()
    noencontro = True
    for i in pelis:
        if caracteristica == i:
            opc = ""
            while opc != "si" and opc != "no":
              opc = input("Deseas borrar la caracteristica? (si/no): ").lower().strip()
            if opc=="si":
                pelis.pop(caracteristica)
                funciones.accionExitosa()
                noencontro = False
    if noencontro:
        input("\n\t...¡No existe la pelicula que andas buscando!...")

def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR LA CARACTERISTICA DE UNA PELICULA ::::...\n")   
    caracteristica=input("Escribe el nombre de la caracteristica: ").upper().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la caracteristica (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteristica que andas buscando!...")

def buscarPeliculas2(pelis):
    caracteristicas = input("Ingresa el nombre de la característica: ").lower().strip()
    noencontro = True

    for i in pelis:
        if caracteristicas == i:
            print("\tCaracteristicas\t\tValor")
            print(f"\t{i}\t\t\t{pelis[i]}")
            noencontro = False
            funciones.espereTecla()
    if noencontro:
            input("\n\t...No se encontro la caracteristica que andas buscando!...")

