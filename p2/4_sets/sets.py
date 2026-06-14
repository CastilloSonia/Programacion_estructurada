"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

set1={"Python","SQL","Estructurado","SQL"}
print(set1)

for i in set1:
    print(i)

# for i in range(0,len(set1)):
#     print()

set2={"Hola", True,33,3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={" "}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)

set3.clear()
print(set3)

set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print(lista)

# Ejemplo crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1

lista_emails=[]
#set_emails={" "}

opc="S"
while opc=="S":
    lista_emails.append(input("Ingresa un email: ").lower().strip())
    #set_emails.add(input("Ingresa un email: ").lower().strip())
    opc=input("¿Deseas ingresar otro email (S/N)?").upper().strip()
print(lista_emails)
#print(set_emails)
set_emails=set(lista_emails)
#print(set_emails)
lista_emails=list(set_emails)
print(lista_emails)

#Solucion 2

emails=[]

resp="True"
while resp:
    emails.insert(0,input("Ingresa un email: ").strip())
    resp=input("¿Deseas ingresar otro email (S/N)?").upper().strip()
    if resp=="N":
        resp=False
emails_set=set(emails)
emails=list(emails_set)
print(emails)

  



