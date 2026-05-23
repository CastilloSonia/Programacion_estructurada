
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("apellido: ").strip().upper()
    print(f"El nombre del alumno es: {nombre} {apellidos}")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre del alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Nombre: ").strip().upper()
    apellidos=input("apellido: ").strip().upper()
    return nombre, apellidos

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    nombre=nom
    apellidos=ape
    return nombre, apellidos

nom,ape=funcion4("Juan", "Lopez")
print(f"El nombre del alumno es: {nom} {ape}")
#Invocar las funciones

funcion1()

nombre=input("Nombre: ").strip().upper()
apellidos=input("apellido: ").strip().upper()
funcion3(nombre, apellidos)

nom,ape=funcion2()
print(f"El nombre del alumno es: {nom} {ape}")

nombre=input("Nombre: ").strip().upper()
apellidos=input("apellido: ").strip().upper()
nom,ape=funcion4(nombre,apellidos)