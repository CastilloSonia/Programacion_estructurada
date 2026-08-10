import time
from rich.console import Console
from rich.prompt import Prompt

from conexion import conectar
import funciones
from usuarios import usuarios
from usuarios import crud as usuarios_crud
from libros import libros
from rentas import rentas

console = Console()

def menuEmpleado(conexionBD, usuarioActual):
    opc = False
    while opc != "0":
        funciones.borrarPantalla()
        
        console.print("[bold cyan]🛠️  .......:::: P A N E L   D E   T R A B A J A D O R :::.......[/bold cyan]")
        console.print(f"[bold cyan]👤 BIENVENIDO:[/bold cyan] [bold white]{usuarioActual['nombre']}[/bold white]\n")
        console.print("  [bold cyan]1)[/bold cyan] 👥 Gestión de usuarios")
        console.print("  [bold cyan]2)[/bold cyan] 📚 Gestión de libros")
        console.print("  [bold cyan]3)[/bold cyan] 🔄 Gestión de rentas")
        console.print("  [bold red]0)[/bold red] 🚪 Cerrar sesión\n")
        
        opc = Prompt.ask("👉 Ingresa la opción a la que deseas ingresar").strip()

        if opc == "1":
            # Submenu para gestionar la tabla de usuarios
            opc_u = ""
            while opc_u != "7":
                funciones.borrarPantalla()
                console.print("[bold blue].......::::  G E S T I O N   D E   U S U A R I O S  ::::.......[/bold blue]\n")
                opc_u = funciones.menuSecundario()

                if opc_u == "1":
                    funciones.borrarPantalla()
                    usuarios.agregar(conexionBD)
                elif opc_u == "2":
                    funciones.borrarPantalla()
                    usuarios.borrarUsuario(conexionBD)
                elif opc_u == "3":
                    funciones.borrarPantalla()
                    usuarios.modificarUsuario(conexionBD)
                elif opc_u == "4":
                    funciones.borrarPantalla()
                    usuarios.mostrarUsuarios(conexionBD)
                elif opc_u == "5":
                    funciones.borrarPantalla()
                    usuarios.buscarUsuarios(conexionBD)
                elif opc_u == "6":
                    funciones.borrarPantalla()
                    usuarios.limpiarUsuarios(conexionBD)
                elif opc_u == "7":
                    funciones.borrarPantalla()
                    console.print("\n[bold green]↩️ Regresando al menú principal...[/bold green]")
                    funciones.espereTecla()
                else:
                    funciones.opcionInvalida()
                    funciones.espereTecla()

        elif opc == "2":
            opc_u = ""
            while opc_u != "7":
                funciones.borrarPantalla()
                console.print("[bold blue].......::::  G E S T I O N   D E   L I B R O S  ::::.......[/bold blue]\n")
                opc_u = funciones.menuSecundario()

                if opc_u == "1":
                    funciones.borrarPantalla()
                    libros.agregar(conexionBD)
                elif opc_u == "2":
                    funciones.borrarPantalla()
                    libros.borrarLibro(conexionBD)
                elif opc_u == "3":
                    funciones.borrarPantalla()
                    libros.modificarLibro(conexionBD)
                elif opc_u == "4":
                    funciones.borrarPantalla()
                    libros.mostrarLibros(conexionBD)
                elif opc_u == "5":
                    funciones.borrarPantalla()
                    libros.buscarLibros(conexionBD)
                elif opc_u == "6":
                    funciones.borrarPantalla()
                    libros.limpiarLibros(conexionBD)
                elif opc_u == "7":
                    funciones.borrarPantalla()
                    console.print("\n[bold yellow]↩️ Regresando al menú principal...[/bold yellow]")
                    funciones.espereTecla()
                else:
                    funciones.opcionInvalida()
                    funciones.espereTecla()

        elif opc == "3":
            # Submenú Gestión de Rentas para Administrador / Empleado
            opc_r = ""
            while opc_r != "3":
                funciones.borrarPantalla()
                
                console.print("[bold blue].......::::  G E S T I O N   D E   R E N T A S  ::::.......[/bold blue]\n")
                console.print("  [bold cyan]1)[/bold cyan] 📋 Ver rentas activas de clientes")
                console.print("  [bold cyan]2)[/bold cyan] 🔄 Procesar devolución de un libro")
                console.print("  [bold red]3)[/bold red] ↩️ Regresar al menú principal\n")

                opc_r = Prompt.ask("👉 Ingresa la opción que deseas (o 0 para regresar)").strip()

                if opc_r == "1":
                    rentas.ver_rentas_generales(conexionBD)
                elif opc_r == "2":
                    rentas.devolver_libro_admin(conexionBD)
                elif opc_r == "3" or opc_r == "0":
                    break
                else:
                    funciones.opcionInvalida()
                    funciones.espereTecla()

        elif opc == "0":
            console.print(f"\n[bold magenta]🔒 Cerrando sesión de {usuarioActual['nombre']}...[/bold magenta]")
            funciones.espereTecla()
        else:
            funciones.opcionInvalida()
            funciones.espereTecla()


def menuCliente(conexionBD, usuarioActual):
    opc = ""
    while opc != "0":
        funciones.borrarPantalla()
        
        console.print("[bold magenta]👤 .......:::: P A N E L   D E   U S U A R I O :::.......[/bold magenta]")
        console.print(f"[bold cyan]👋 BIENVENIDO:[/bold cyan] [bold white]{usuarioActual['nombre']}[/bold white]\n")
        console.print("  [bold cyan]1.[/bold cyan] 📖 Ver Catálogo de Libros")
        console.print("  [bold cyan]2.[/bold cyan] 🔖 Rentar un Libro")
        console.print("  [bold cyan]3.[/bold cyan] 📋 Ver Mis Rentas Activas")
        console.print("  [bold cyan]4.[/bold cyan] 🔄 Devolver un Libro")
        console.print("  [bold red]0.[/bold red] 🚪 Cerrar Sesión\n")
        
        opc = Prompt.ask("👉 Ingresa la opción a la que deseas ingresar").strip()
        
        if opc == "1":
            funciones.borrarPantalla()
            libros.mostrarLibros(conexionBD)
        elif opc == "2":
            funciones.borrarPantalla()
            # Pasamos usuarioActual para saber si es estudiante y calcular las fechas
            rentas.solicitar_renta(conexionBD, usuarioActual)
        elif opc == "3":
            funciones.borrarPantalla()
            rentas.mis_rentas(conexionBD, usuarioActual)
        elif opc == "4":
            funciones.borrarPantalla()
            rentas.devolver_libro(conexionBD, usuarioActual)
        elif opc == "0":
            console.print(f"\n[bold cyan]👋 Hasta luego, {usuarioActual['nombre']}. Cerrando sesión...[/bold cyan]")
            funciones.espereTecla()
        else:
            funciones.opcionInvalida()
            funciones.espereTecla()


# EJECUCION DEL PROGRAMA
with console.status("[bold green]Conectando a la Base de Datos...", spinner="dots"):
    conexionBD = conectar()
    time.sleep(0.1)

if conexionBD is not None:
    opcion_principal = ""

    funciones.bienvenida_creativa()
    while opcion_principal != "0":
        funciones.borrarPantalla()
        
        console.print("\t\t[bold bright_green] .......:::: S I S T E M A  D E  B I B L I O T E C A ::::.......[/bold bright_green]\n")
        console.print("  [bold green]1.[/bold green] 🔑 Iniciar Sesión")
        console.print("  [bold green]2.[/bold green] 📝 Registrarse (Crear cuenta de usuario)")
        console.print("  [bold red]0.[/bold red] 🚪 Salir\n")
        
        opcion_principal = Prompt.ask("👉 Selecciona una opción").strip()

        if opcion_principal == "1":
            funciones.borrarPantalla()
            console.print("[bold cyan]...:::: INICIO DE SESIÓN ::::...[/bold cyan]\n")
            correo = Prompt.ask("📧 Ingresa tu correo electrónico (o 0 para regresar)").strip()
            
            if funciones.cancelarOperacion(correo):
                continue

            # Buscamos el correo a través de la función del crud en la base de datos
            with console.status("[bold yellow]Verificando credenciales...", spinner="dots"):
                busqueda = usuarios_crud.buscar_por_correo(correo, conexionBD)
                time.sleep(0.5)

            if len(busqueda) > 0:
                usuarioLogueado = busqueda[0]
                console.print(f"\n[bold green]✨ ¡Bienvenido de nuevo, {usuarioLogueado['nombre']}![/bold green]")
                funciones.espereTecla()

                if usuarioLogueado['rol'] == "EMPLEADO":
                    menuEmpleado(conexionBD, usuarioLogueado)
                else:
                    menuCliente(conexionBD, usuarioLogueado)
            else:
                console.print("\n[bold red]❌ El correo ingresado no está registrado en el sistema.[/bold red]")
                funciones.espereTecla()
                
        elif opcion_principal == "2":
            funciones.borrarPantalla()
            # Registro público para nuevos clientes
            console.print("[bold cyan]...:::: REGISTRO DE NUEVO CLIENTE :::...[/bold cyan]\n")
            usuarios.agregar(conexionBD, es_publico=True)
            
        elif opcion_principal == "0":
            funciones.despedida_creativa()
            conexionBD.close()  # Cerramos la conexión a la BD al salir
            
        else:
            funciones.opcionInvalida()
            funciones.espereTecla()
else:
    console.print("[bold red]❌ Error: No se pudo establecer la conexión con la base de datos.[/bold red]")