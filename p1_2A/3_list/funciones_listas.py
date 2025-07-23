"""
list (Array)
Son colecciones o conjunto de datos/valores bajo un mismp nombre. para acceder a los valores se hace con un indice numerico

Nota: Sus valores si son modificables 

La lista es una coleccon ordenada y modificable. Permite miembros duplicados.

"""

import os 
os.system("clear")

#Funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros = [23,12,100,34]

varios = ["Hola",True,33,3.12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)

#Agregar o isnertar o añadir un elemanto a la listas
#primer forma paises=("Mexico","Brasil","España","Canada")
print(paises)
paises.append("Honduras")
print(paises)

#Forma 2
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o suprimir un elemanto a la listas
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Honduras")
print(paises)


#Buscar un elemanto
#paises=("Mexico","Brasil","España","Canada")

print("Brasil" in paises)

#contar el numero de veces que un elemento esta dentor de una lista
#numeros=(23,12,100,34)
print(numeros)
print(numeros.count (12))
numeros.insert(1,12)
print(numeros)
print(numeros.count (12))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(paises)
print(numeros)

# Conocer el índice o la pocisión de un valor de la lsta.
pocision = paises.index("España")

# Unir el contenido de 2 o más listas en una sola.
# numeros = [100, 34, 23, 12, 12]
numeros2 = [300, 500, 100]

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)