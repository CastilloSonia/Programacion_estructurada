from paquete1 import modulos,modulo_paquete
modulos.borrarPantalla()

nom="Juan"
ape="Polainas"

nombre,apellidos,edad=modulos.funcion4(nom,ape)
edad=modulo_paquete.solicitarEdad()

print(f"Nombre: {nombre}\nApellidos: {apellidos}\nEdad: {edad}")