import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

import funciones
from libros import crud

console = Console()


def agregar(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: AGREGAR LIBRO ::::.......[/bold yellow]\n")

    titulo = Prompt.ask("📖 Ingrese título del libro (o 0 para cancelar)").upper().strip()
    if funciones.cancelarOperacion(titulo):
        return
    autor = Prompt.ask("✍️ Ingrese autor del libro").upper().strip()
    categoria = Prompt.ask("🏷️ Ingrese categoría").upper().strip()

    stock = Prompt.ask("📦 Ingrese cantidad de ejemplares (Stock)").strip()
    while not stock.isdigit() or int(stock) < 0:
        console.print("[bold red]⚠️ Opción no válida. Ingrese un número entero positivo.[/bold red]")
        funciones.espereTecla()
        funciones.borrarPantalla()
        stock = Prompt.ask("📦 Ingrese cantidad de ejemplares (Stock)").strip()

    with console.status("[bold green]Guardando libro en el catálogo...", spinner="dots"):
        respuesta = crud.insertar(titulo, autor, categoria, int(stock), conexionBD)
        time.sleep(0.5)

    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()


def mostrarLibros(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: CATÁLOGO DE LIBROS ::::.......[/bold yellow]\n")

    with console.status("[bold yellow]Consultando libros...", spinner="dots"):
        libros = crud.consultar(conexionBD)
        time.sleep(0.4)

    if len(libros) > 0:
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Título", style="bold white")
        tabla.add_column("Autor", style="yellow")
        tabla.add_column("Categoría", style="magenta")
        tabla.add_column("Stock", justify="center")

        for i in libros:
            stock_style = f"[bold green]{i['stock']}[/bold green]" if i['stock'] > 0 else "[bold red]0[/bold red]"
            tabla.add_row(str(i['id']), i['titulo'], i['autor'], i['categoria'], stock_style)

        console.print(tabla)
    else:
        console.print("[bold yellow]⚠️ No hay libros actualmente para mostrar.[/bold yellow]")

    funciones.espereTecla()


def buscarLibros(conexionBD):
    opcion = ""
    while opcion not in ["1", "2", "3", "4"]:
        funciones.borrarPantalla()
        console.print("[bold yellow].......:::: BUSCAR LIBROS ::::.......[/bold yellow]\n")
        console.print("  [bold cyan]1)[/bold cyan] 📖 Buscar por título")
        console.print("  [bold cyan]2)[/bold cyan] ✍️ Buscar por autor")
        console.print("  [bold cyan]3)[/bold cyan] 🏷️ Buscar por categoría")
        console.print("  [bold red]4)[/bold red] ↩️ Regresar\n")
        
        opcion = Prompt.ask("👉 ¿Por qué método desea hacer la búsqueda?").strip()
        if opcion not in ["1", "2", "3", "4"]:
            funciones.opcionInvalida()

    resultados = []

    if opcion == "1":
        funciones.borrarPantalla()
        console.print("[bold yellow].......:::: BUSCAR POR TÍTULO ::::.......[/bold yellow]\n")
        titulo = Prompt.ask("📖 Ingresa el título").upper().strip()
        with console.status("[bold yellow]Buscando en el catálogo...", spinner="dots"):
            resultados = crud.buscar_por_titulo(titulo, conexionBD)
            time.sleep(0.4)

    elif opcion == "2":
        funciones.borrarPantalla()
        console.print("[bold yellow].......:::: BUSCAR POR AUTOR ::::.......[/bold yellow]\n")
        autor = Prompt.ask("✍️ Ingresa el autor").upper().strip()
        with console.status("[bold yellow]Buscando en el catálogo...", spinner="dots"):
            resultados = crud.buscar_por_autor(autor, conexionBD)
            time.sleep(0.4)

    elif opcion == "3":
        funciones.borrarPantalla()
        console.print("[bold yellow].......:::: BUSCAR POR CATEGORÍA ::::.......[/bold yellow]\n")
        categoria = Prompt.ask("🏷️ Ingresa la categoría").upper().strip()
        with console.status("[bold yellow]Buscando en el catálogo...", spinner="dots"):
            resultados = crud.buscar_por_categoria(categoria, conexionBD)
            time.sleep(0.4)

    elif opcion == "4":
        return

    if len(resultados) > 0:
        funciones.borrarPantalla()
        console.print("[bold yellow].......:::: RESULTADOS ENCONTRADOS ::::.......[/bold yellow]\n")
        
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Título", style="bold white")
        tabla.add_column("Autor", style="yellow")
        tabla.add_column("Categoría", style="magenta")
        tabla.add_column("Stock", justify="center")

        for i in resultados:
            stock_style = f"[bold green]{i['stock']}[/bold green]" if i['stock'] > 0 else "[bold red]0[/bold red]"
            tabla.add_row(str(i['id']), i['titulo'], i['autor'], i['categoria'], stock_style)

        console.print(tabla)
    else:
        console.print("\n[bold yellow]⚠️ No se encontraron libros con ese criterio de búsqueda.[/bold yellow]")

    funciones.espereTecla()


def modificarLibro(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: MODIFICAR LIBRO ::::.......[/bold yellow]\n")

    id_libro = Prompt.ask("🔍 Escribe el ID del libro a modificar").strip()

    with console.status("[bold yellow]Buscando libro...", spinner="dots"):
        libro = crud.buscar_por_id(id_libro, conexionBD)
        time.sleep(0.4)

    if libro is not None:
        console.print(f"\n📌 [bold cyan]Libro encontrado:[/bold cyan] [bold white]{libro['titulo']}[/bold white] — [yellow]Autor:[/yellow] {libro['autor']}\n")

        titulo_new = Prompt.ask("📖 Nuevo título").upper().strip()
        autor = Prompt.ask("✍️ Nuevo autor").upper().strip()
        categoria = Prompt.ask("🏷️ Nueva categoría").upper().strip()

        stock = Prompt.ask("📦 Nuevo stock (cantidad)").strip()
        while not stock.isdigit() or int(stock) < 0:
            console.print("[bold red]⚠️ Opción no válida. Ingrese un número entero.[/bold red]")
            stock = Prompt.ask("📦 Nuevo stock (cantidad)").strip()

        with console.status("[bold green]Actualizando libro...", spinner="dots"):
            respuesta = crud.actualizar(titulo_new, autor, categoria, int(stock), libro['id'], conexionBD)
            time.sleep(0.5)

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        console.print("\n[bold red]⚠️ No existe ningún libro registrado con ese ID.[/bold red]")

    funciones.espereTecla()


def borrarLibro(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: BORRAR LIBRO ::::.......[/bold yellow]\n")

    with console.status("[bold yellow]Cargando libros...", spinner="dots"):
        libros = crud.consultar(conexionBD)
        time.sleep(0.4)

    if len(libros) > 0:
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Título", style="bold white")
        tabla.add_column("Autor", style="yellow")
        tabla.add_column("Categoría", style="magenta")
        tabla.add_column("Stock", justify="center")

        for i in libros:
            stock_style = f"[bold green]{i['stock']}[/bold green]" if i['stock'] > 0 else "[bold red]0[/bold red]"
            tabla.add_row(str(i['id']), i['titulo'], i['autor'], i['categoria'], stock_style)

        console.print(tabla)
    else:
        console.print("[bold yellow]⚠️ No hay libros actualmente para borrar.[/bold yellow]")

    id_libro = Prompt.ask("\n🎯 Escribe el ID del libro a borrar (o 0 para cancelar)").strip()
    if id_libro == "0":
        console.print("\n[bold yellow]⚠️ Operación cancelada.[/bold yellow]")
        funciones.espereTecla()
        return

    with console.status("[bold yellow]Buscando libro...", spinner="dots"):
        libro = crud.buscar_por_id(id_libro, conexionBD)
        time.sleep(0.4)

    if libro is not None:
        console.print(f"\n📌 [bold cyan]ID:[/bold cyan] {libro['id']} | [bold white]{libro['titulo']}[/bold white] | [yellow]{libro['autor']}[/yellow]")
        opc = Prompt.ask("\n❓ ¿Deseas borrar este libro? (Si/No)").lower().strip()
        
        while opc not in ["si", "no"]:
            funciones.opcionInvalida()
            funciones.espereTecla()
            funciones.borrarPantalla()
            opc = Prompt.ask("\n❓ ¿Deseas borrar este libro? (Si/No)").lower().strip()

        if opc == "si":
            with console.status("[bold red]Eliminando libro...", spinner="bouncingBar"):
                respuesta = crud.borrar(libro['id'], conexionBD)
                time.sleep(0.5)

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNOExitosa()
    else:
        console.print("\n[bold red]⚠️ No existe ningún libro con ese ID.[/bold red]")

    funciones.espereTecla()


def limpiarLibros(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold red].......:::: VACIAR CATÁLOGO DE LIBROS ::::.......[/bold red]\n")

    with console.status("[bold yellow]Consultando catálogo...", spinner="dots"):
        libros = crud.consultar(conexionBD)
        time.sleep(0.4)

    if len(libros) > 0:
        console.print("[bold red]⚠️ ADVERTENCIA:[/bold red] Esta acción borrará [bold red]TODOS[/bold red] los libros registrados.\n")
        opc = Prompt.ask("❓ ¿Deseas borrar TODOS los libros? (Si/No)").lower().strip()

        while opc not in ["si", "no"]:
            funciones.opcionInvalida()
            funciones.espereTecla()
            opc = Prompt.ask("❓ ¿Deseas borrar TODOS los libros? (Si/No)").lower().strip()

        if opc == "si":
            with console.status("[bold red]Limpiando catálogo de libros...", spinner="bouncingBar"):
                respuesta = crud.vaciar(conexionBD)
                time.sleep(2)

            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNOExitosa()
    else:
        console.print("[bold yellow]⚠️ No hay libros agregados para borrar...[/bold yellow]")

    funciones.espereTecla()
    funciones.borrarPantalla()
   