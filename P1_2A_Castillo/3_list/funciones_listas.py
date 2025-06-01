"""
List (array)
 son colleciones o conjunto de datos/valores bajo un mismo
nombre, para acceder a los valores se hace con un indice
numerico
nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. permite miembros duplicados.
"""
import os 
os.system("clar")

#funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

varios=["Hola",True,33,3.12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)
#agrega o insertar oañadir un elemento analista
#1er forma
print(paises)
paises.append("Honduras")
print(paises)
#se puede duplicar
#2da forma 
paises.insert(1,"Honduras")
print(paises)
#Eliminar o borrar o suprimir un elemnto a la lista 
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un Elemento dentro de una lista
print("Brasil" in paises)

#contar el numero Veces que un elemento esta dentro de una lista 
#numero=[23,12,100,34]
print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(101))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(numeros)
print(paises)

#conoser el indice o la posicion de un valor de la lista
posicion=paises.index("España")

#unir el contenido de 2 o mas  Listas en una sola
#numeos=[100,34,23,12,12]
numeros2=[300,500,100]
print(numeros)
print(numeros2)
numeros. extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)
