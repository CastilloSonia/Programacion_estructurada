peliculas=[]
contraseña = "angelo1"  

#dict u objetos para los atributos (Nombre, Categoria, clasificacion, genero, idioma)

#peliculas={
#            "nombre":"",
#            "Categorias":"",
#            "clasificasion":"",
#            "genero":"",
#           "idiomas":""
#           }

pelicula={}
def borrarPantalla():
    import os
    os.system("crear")

def esperarTecla():
    input("Oprima culaquier tecla para continuar ...")   

def CrearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de peliculas ::.\n ")
    #pelicula["nombre"]=input("Ingresa el nombre: ").ipper().strip
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().split()})
    pelicula.update({"categoria":input("Ingresa la Categoria: ").upper().split()})
    pelicula.update({"clasificasion":input("Ingresa la clasificacion: ").upper().split()})
    pelicula.update({"genero":input("Ingresa el Genero: ").upper().split()})
    pelicula.update({"idioma":input("Ingresa el Idioma").upper().split()})
    input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")


def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la pelicula ::.\n ")
    if len (pelicula)>0:
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
    else:
        print("\t .:: No hay peliculas en el sistema ::.")

def borrarpeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o quitar todas las peliculas ::.\n ")
    resp=input("¿Deseas Quitar todas las peliculas del sistema (si/no) ")
    if resp=="si":
        peliculas.clear()
        print("\n\t\t ::: ¡LA OPERACION SE REALISO CON EXITO! :::")

def agregarCaracteristucapeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Caracteristica a peliculas ::.\n ")
    atributo=input("Ingresar la nueva caracteristica de la pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    #pelicula.update({atributo:valor})
    pelicula[atributo]=valor
    print("\n\t\t ::: ¡LA OPERACION SE REALISO CON EXITO! :::")

def modificarCaracteristicaPeliculas():
   borrarPantalla()
   print("\n\t.:: Modificar Características a Películas  ::. \n")
   if len(pelicula)>0:
    print(f"\n\tValor actuales: \n ")
    for i in pelicula:
      print(f"\t {(i)} : {pelicula[i]}")
      resp=input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
      if resp=="si":
        pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
   else:
      print("\t..:: No hay peliculas en Sistema  ::..")


def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Película ::.\n ")
    if len(pelicula) == 0:
        print("\t .:: No hay información de películas registrada ::.")
        return
    intento = input("Ingresa la contraseña para continuar: ").strip()
    if intento != contraseña:
        print("\n\t  Contraseña incorrecta. No se puede continuar.")
        return
    print("Características actuales:")
    for clave in pelicula:
        print(f" - {clave} : {pelicula[clave]}")

    clave = input("\nIngresa el nombre de la característica que deseas eliminar: ").lower().strip()
    if clave in pelicula:
        del pelicula[clave]
        print("\n\t\t ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        print("\n\t ::: ¡La característica no existe! :::")
