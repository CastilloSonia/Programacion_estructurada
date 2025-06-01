#import 0s; se utilisa para solo imprimir tu documento
#ejemplo 1 crear una lista de numeros e imprimir el contenido
numero=[25,36,87,20]
print(numero)
#2da forma trabajo con el valor 
for i in numero:
    print(i)
#3ra forma, trabaja con el indices
for i in range(0,len(numero)):
    print(numero[i])
 #ejemplo 2 crear una lista de palabras y posteriormente  buscar la cinsidencia de una palabra

palabras=["Hola","pablo","neptuno","hello"]

palabras_buscar=input("Dame la palabra a buscar")
#1er forma
if palabras_buscar in palabras:
    print("se encontro la palabra ")
else:
    print("no encontro la palabra ")

#2da forma
encontro= False
for i in palabras:
    if i==palabras_buscar:
         encontro=True

if encontro:
    print("se encontro la palabra")
else:
    print("No encontro la palabra")

#3ra forma 
encontro= False
for i in palabras:
    if palabras_buscar:
         encontro=True

if encontro:
    print("se encontro la palabra")
else:
    print("No encontro la palabra")





#elemplo 3 añadir elementos a la lista
numeros=[]
print(numeros)

opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal: ")) 
    numeros.append(numero)
    resp=input("Deseas agregar otro numero?: ").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)

input("Oprima una tecla para continuar")    



#ejemplo 4 crear una lista multidemcional (matriz) que almacena el nombre y telefono de 4 personas
agenda=[
    ["Carlos","6181234567"],
    ["Alberto","6671234567"],
    ["Martin","6785678923"]
        ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena += f"{agenda[r][c]},"
    cadena+="\n"
print(cadena)    