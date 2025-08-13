from Clientes.clientes import menu_clientes
from Inventario.inventario import menu_inventario
from Venta.ventas import menu_ventas
from funciones import limpiar_pantalla, esperar_tecla, crear_tablas
from autenticacion import menu_autenticacion

def main():
    # 🏗️ Configuración inicial
    crear_tablas()
    
    # 🔐 Autenticación
    usuario_actual = menu_autenticacion()
    
    if not usuario_actual:
        return
    
    # 🎛️ Menú principal
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(f" 👋 BIENVENIDO, {usuario_actual['nombre'].upper()} ".center(50, "="))
        print("=" * 50)
        print("1. 👥 Gestión de Clientes")
        print("2. 📦 Gestión de Inventario")
        print("3. 💰 Gestión de Ventas")
        
        if usuario_actual['rol'] == 'admin':
            print("4. 👑 Administración de usuarios")
            
        print("5. 🔄 Cerrar sesión")
        print("6. 🚪 Salir del sistema")
        print("=" * 50)
        
        opcion = input("👉 Seleccione una opción: ")
        
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_inventario()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4" and usuario_actual['rol'] == 'admin':
            print("\n🛠️ (Próximamente) Menú de administración de usuarios")
            esperar_tecla()
        elif opcion == "5":
            print("\n🔒 Sesión cerrada correctamente")
            usuario_actual = menu_autenticacion()
            if not usuario_actual:
                break
        elif opcion == "6":
            print("\n👋 ¡Hasta pronto!")
            break
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")
            esperar_tecla()

if __name__ == "__main__":
    main()