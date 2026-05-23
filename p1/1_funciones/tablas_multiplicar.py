'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

num_tabla=int(input("Numero de la tabla de multiplicar: "))

num=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num}  = {multi} ")
num+=1


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control solo while
  2.- Sin funciones

'''
print("\033c")

num_tabla=int(input("Numero de la tabla de multiplicar: "))

for num in range(1,11):
  multi=num_tabla*num
  print(f"{num_tabla} x {num}  = {multi} ")
  
num=1
while num<11:
  multi=num_tabla*num
  print(f"{num_tabla} x {num}  = {multi} ")
  num+=1
  
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control 
  2.- Con funciones

'''
print("\033c")
def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
    
num_tabla=int(input("Numero de la tabla de multiplicar: "))
num=1

n=tabla(num_tabla,num)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control 
  2.- Con funciones

'''

print("\033c")
def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
    
num_tabla=int(input("Numero de la tabla de multiplicar: "))
n=1

for i in range(10,0,-1):
  n=tabla(num_tabla,n)