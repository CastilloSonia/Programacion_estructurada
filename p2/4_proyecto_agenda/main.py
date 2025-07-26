
import agenda

def main():
    datos = []
    opcion = True
    while opcion:
        agenda.borrarPantalla()
        opcion= agenda.menu_Principal()
        match opcion:
            case "1":
                agenda.AgregarContactos(datos)
                agenda.esperarTecla()
            case "2":
                agenda.MostrarContactos(datos)
                agenda.esperarTecla()
            case "3":
                agenda.BuscarContactos(datos)
                agenda.esperarTecla() 
            case "4":
                agenda.ModificarContacto(datos)
                agenda.esperarTecla()
            case "5":
                agenda.EliminarContacto(datos)
                agenda.esperarTecla()
            case "6":
                opcion = False
                print("\n\tTerminaste la ejecución del programa.")
            case _:
                input("\n\t Opción inválida. Presiona Enter para intentarlo de nuevo.")

if __name__ == "__main__":
    main()