import os
# Ejemplo 1 crear una lista de números e imprimir el contenido.

os.system ("clear")

numeros = [23, 45, 8, 24]

# 1er forma.
print(numeros)

# 2da forma.
for i in numeros:
    print(i)

# 3er forma.
for i in range(0, len(numeros)):
    print(numeros[i])

# Ejemplo 2: Crear una lista de palabras y posteriormente buscar la coincidencia de una palabea.
os.system("clear")

palabras = ["Hola", "Adios", "Dia", "Sol"]

print(palabras)
"""
print("Sol" in palabras)
"""
# 1er forma.
palabra_buscar= input("Dame la palabra a buscar: ")
if palabra_buscar in palabras:
    print("Se encontró la palabra.")
else:
    print("No se encontró la palabra.")

# 2da forma
encontro = False
for i in palabras:
    if i == palabra_buscar:
        encontro = True
        
if encontro:      
        print("Se encontró la palabra.")
else:
        print("No se encontró la palabra.")

# 3er forma
encontro = False
for i in range(0, len (numeros)):
    if palabras[i] == palabra_buscar:
        encontro = True
        
if encontro:      
        print("Se encontró la palabra.")
else:
        print("No se encontró la palabra.")

# Ejemplo 3: Añadir elementos a una lista.
os.system("clear")
numeros = []
opc = "si"
while opc =="si":
     numeros.append=(float(input("Ingresa un número entero o decimal")))
     opc = input("¿Deseas solicitar otro número (si/no)").lower()
print(numeros)

# Ejemplo 4: Crear una lista multidimensional (matriz) que almacene el nombre y teléfono de 4 personas.

agenda = [
    ["Carlos", "1234567890"],
    ["Alberto", "9876543210"],
    ["Martín", "5551234567"],
]

print(agenda)

# Acceder a los datos
for i in agenda:
    print(f"Nombre: {i[0]}, Teléfono: {i[1]}")

