from funciones import *

def menu_autenticacion():
    """🎭 Menú de autenticación del sistema"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" 🛍️ SISTEMA DE TIENDA DE ROPA ".center(50, "="))
        print("=" * 50)
        print("1. 🔑 Iniciar sesión")
        print("2. 👤 Registrarse")
        print("3. 🚪 Salir")
        print("=" * 50)
        
        opcion = input("👉 Seleccione una opción: ")
        
        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                return usuario
        elif opcion == "2":
            if registrar_usuario():
                usuario = iniciar_sesion()
                if usuario:
                    return usuario
        elif opcion == "3":
            print("\n👋 ¡Hasta pronto!")
            exit()
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            esperar_tecla()