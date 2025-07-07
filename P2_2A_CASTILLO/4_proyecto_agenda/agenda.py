
agenda=[]
agenda={}
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima culaquier tecla para continuar ...")

def menu_Principal():
           print("\n\t\t\t..:::  `\U0001F552`Sistema de Gestión de Agenda de contagtos :::...\n 1️⃣.- Agregar contactos  \n 2️⃣.- Mostrar todos los contagtos \n  3️⃣.- Buscar Contagtos por nombre \n 4️⃣.-Modificar Contacto \n 5️⃣.-Eliminar Contactos \n 6️⃣.-SALIR ")
           opcion = input("\t 👉Elige una opción (1-4): ").strip()
           return opcion

def AgregarContactos(lista):
    nombre = input("Nombre del contacto: ").strip().capitalize()
    telefono = input("\U0001F4DETeléfono: ").strip()
    correo = input("\U0001F4E7Correo electrónico: ").strip()
    contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
    lista.append(contacto)
    print("\n✅ Contacto agregado con éxito.")

def MostrarContactos(lista):
    if not lista:
        print("\n❌ No hay contactos para mostrar.")
    else:
        print("\n📒 Lista de contactos:")
        for i, contacto in enumerate(lista, start=1):
            print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")

def BuscarContactos(lista):
    nombre = input("🔍 Ingresa el nombre a buscar: ").strip().capitalize()
    encontrados = [c for c in lista if c['nombre'] == nombre]
    if encontrados:
        print("\n✅ Contactos encontrados:")
        for c in encontrados:
            print(f"{c['nombre']} - {c['telefono']} - {c['correo']}")
    else:
        print("\n❌ No se encontró ningún contacto con ese nombre.")

def ModificarContacto(lista):
    borrarPantalla()
    print("📝 Modificar Contacto")
    if not lista:
        print("❌ No hay contactos")
    else:
        nombre = input("🔍 Nombre del contacto a modificar: ").strip().capitalize()
        for contacto in lista:
            if contacto["nombre"] == nombre:
                print(f"\n📌 Contacto encontrado: {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")
                resp = input("¿Deseas modificar este contacto? (si/no): ").strip().lower()
                if resp == "si":
                    contacto["telefono"] = input("\U0001F4DENuevo teléfono: ").strip()
                    contacto["correo"] = input("\U0001F4E7Nuevo correo: ").strip()
                    print("✅ Contacto modificado con éxito.")
                return
        print("❌ No se encontró ningún contacto con ese nombre.")

def EliminarContacto(lista):
    borrarPantalla()
    print("🗑️ Eliminar Contacto")
    if not lista:
        print("❌ No hay contactos en la agenda.")
    else:
        nombre = input("🔍 Nombre del contacto a eliminar: ").strip().capitalize()
        for i, contacto in enumerate(lista):
            if contacto["nombre"] == nombre:
                print(f"\n📌 Contacto encontrado: {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")
                resp = input("¿Deseas eliminar este contacto? (si/no): ").strip().lower()
                if resp == "si":
                    lista.pop(i)
                    print("✅ Contacto eliminado con éxito.")
                return
        print("❌ No se encontró ningún contacto con ese nombre.")
