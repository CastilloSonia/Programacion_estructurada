# 1er forma de utilizar los modulos .
import modulos

modulos.borrarPantalla()

n="Daniel"
a="Carreon"

nombre,apellidos= modulos.funcion4(n,a)
print(f"El nombre completo es: {nombre} {apellidos}")


#2da forma de utilizar modulos.

from modulos import borrarPantalla, funcion2,funcion3

borrarPantalla()
n="Daniel"
a="Carreon"
funcion3(n,a)

nombre, apellidodo=funcion2()
print(f"El nombre completo es: {nombre} {apellidodo}")  