import agenda

def main():
    # Verificar conexión inicial
    agenda.borrarPantalla()
    print("\nVerificando conexión con la base de datos...")
    conexion = agenda.conectar()
    if conexion:
        if conexion.is_connected():
            conexion.close()
        print("\nConexión establecida correctamente")
    else:
        print("\nNo se pudo conectar a la base de datos")
    agenda.esperarTecla()
    
    while True:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()
        
        if opcion == "1":
            agenda.agregar_contacto()
        elif opcion == "2":
            agenda.mostrar_contactos()
        elif opcion == "3":
            agenda.buscar_contacto()
        elif opcion == "4":
            agenda.modificar_contacto()
        elif opcion == "5":
            agenda.borrar_contacto()
        elif opcion == "6":
            agenda.inicializar_bd()
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida")
        
        agenda.esperarTecla()

if __name__ == "__main__":
    main()