import time
from datetime import date, timedelta
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

import funciones
from rentas import crud as rentas_crud
from libros import crud as libros_crud

console = Console()


# Genera un archivo txt con el comprobante de la renta
def generar_ticket_txt(usuario_nombre, libro_titulo, fecha_renta, fecha_devolucion):
    try:
        nombre_limpio = usuario_nombre.replace(' ', '_')
        nombre_archivo = f"ticket_renta_{nombre_limpio}.txt"
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("==================================================\n")
            archivo.write("         COMPROBANTE DE RENTA DE LIBRO            \n")
            archivo.write("==================================================\n")
            archivo.write(f" Cliente:           {usuario_nombre}\n")
            archivo.write(f" Libro Rentado:     {libro_titulo}\n")
            archivo.write(f" Fecha de Renta:    {fecha_renta}\n")
            archivo.write(f" Fecha Límite Dev:  {fecha_devolucion}\n")
            archivo.write("==================================================\n")
            archivo.write("     ¡Gracias por utilizar la biblioteca!         \n")
            archivo.write("==================================================\n")
            
        console.print(f"\n[bold green]📄 Ticket generado exitosamente: '{nombre_archivo}'[/bold green]")
    except Exception as e:
        console.print(f"\n[bold red]❌ No se pudo generar el archivo TXT: {e}[/bold red]")


# Rentas para los clientes
def solicitar_renta(conexionBD, usuarioActual):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: SOLICITAR RENTA DE LIBRO :::.......[/bold yellow]\n")

    id_libro = Prompt.ask("📖 Ingrese el ID del libro que desea rentar (o 0 para cancelar)").strip()
    if funciones.cancelarOperacion(id_libro):
        return

    with console.status("[bold yellow]Buscando libro...", spinner="dots"):
        libro = libros_crud.buscar_por_id(id_libro, conexionBD)
        time.sleep(0.4)

    if libro is None:
        console.print("\n[bold red]❌ El libro ingresado no existe en el catálogo.[/bold red]")
        funciones.espereTecla()
        return

    if libro['stock'] <= 0:
        console.print(f"\n[bold yellow]⚠️ Lo sentimos, '{libro['titulo']}' no tiene ejemplares disponibles.[/bold yellow]")
        funciones.espereTecla()
        return

    fecha_hoy = date.today()

    # Calcular días según el tipo de usuario
    if usuarioActual['estudiante'].upper() == "SI":
        dias_prestamo = funciones.DIAS_PRESTAMO_ESTUDIANTE
    else:
        dias_prestamo = funciones.DIAS_PRESTAMO_GENERAL

    fecha_devolucion = fecha_hoy + timedelta(days=dias_prestamo)

    console.print("\n[bold cyan]📋 RESUMEN DE LA RENTA[/bold cyan]")
    console.print(f"  • [bold white]Libro:[/bold white] {libro['titulo']}")
    console.print(f"  • [bold white]Usuario:[/bold white] {usuarioActual['nombre']}")
    console.print(f"  • [bold white]Fecha de Renta:[/bold white] {fecha_hoy}")
    console.print(f"  • [bold white]Fecha Límite de Devolución:[/bold white] [bold yellow]{fecha_devolucion}[/bold yellow] ({dias_prestamo} días de préstamo)")

    # Contador decremental de días
    contador_dias = dias_prestamo
    while contador_dias > 0:
        contador_dias -= 1

    confirmacion = Prompt.ask("\n❓ ¿Desea confirmar el préstamo? (Si/No)").upper().strip()

    if confirmacion == "SI":
        with console.status("[bold green]Procesando renta...", spinner="dots"):
            exito = rentas_crud.insertar(usuarioActual['id'], libro['id'], fecha_hoy, fecha_devolucion, funciones.ESTADO_ACTIVO, conexionBD)
            time.sleep(0.5)

        if exito:
            nuevo_stock = libro['stock'] - 1
            libros_crud.actualizar_stock(libro['id'], nuevo_stock, conexionBD)
            
            # Crear ticket txt
            generar_ticket_txt(usuarioActual['nombre'], libro['titulo'], fecha_hoy, fecha_devolucion)
            
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        console.print("\n[bold yellow]⚠️ Operación cancelada por el usuario.[/bold yellow]")
        funciones.espereTecla()


def mis_rentas(conexionBD, usuarioActual):
    funciones.borrarPantalla()
    console.print(f"[bold yellow].......:::: RENTAS DE {usuarioActual['nombre']} :::.......[/bold yellow]\n")

    with console.status("[bold yellow]Consultando historial de rentas...", spinner="dots"):
        rentas_lista = rentas_crud.buscar_id_usuario(usuarioActual['id'], conexionBD)
        time.sleep(0.4)

    if len(rentas_lista) > 0:
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID Renta", justify="center", style="cyan")
        tabla.add_column("Título del Libro", style="bold white")
        tabla.add_column("Fecha Renta", justify="center", style="yellow")
        tabla.add_column("Fecha Dev.", justify="center", style="yellow")
        tabla.add_column("Estado", justify="center")

        for r in rentas_lista:
            estado_style = "[bold green]ACTIVA[/bold green]" if r['estado'] == funciones.ESTADO_ACTIVO else "[dim]DEVUELTO[/dim]"
            tabla.add_row(str(r['id']), r['titulo'], str(r['fecha_renta']), str(r['fecha_devolucion']), estado_style)

        console.print(tabla)
    else:
        console.print("[bold yellow]⚠️ No tienes rentas registradas actualmente.[/bold yellow]")

    funciones.espereTecla()


def devolver_libro(conexionBD, usuarioActual):
    funciones.borrarPantalla()
    console.print(f"[bold yellow].......:::: DEVOLUCIÓN DE LIBROS - {usuarioActual['nombre']} :::.......[/bold yellow]\n")

    with console.status("[bold yellow]Cargando rentas activas...", spinner="dots"):
        rentas_activas = rentas_crud.buscar_activas_por_usuario(usuarioActual['id'], conexionBD)
        time.sleep(0.4)

    if len(rentas_activas) == 0:
        console.print("[bold green]✨ No tienes libros pendientes por devolver.[/bold green]")
        funciones.espereTecla()
        return

    tabla = Table(header_style="bold magenta", border_style="cyan")
    tabla.add_column("ID Renta", justify="center", style="cyan")
    tabla.add_column("Título del Libro", style="bold white")
    tabla.add_column("Fecha Dev.", justify="center", style="yellow")
    tabla.add_column("Estado", justify="center", style="bold green")

    for r in rentas_activas:
        tabla.add_row(str(r['id']), r['titulo'], str(r['fecha_devolucion']), r['estado'])

    console.print(tabla)

    ids_validos = [str(r['id']) for r in rentas_activas]
    id_renta = Prompt.ask("\n🎯 Ingrese el ID de la renta que desea devolver (o 0 para cancelar)").strip()

    while id_renta != "0" and id_renta not in ids_validos:
        funciones.opcionInvalida()
        id_renta = Prompt.ask("🎯 Ingrese el ID de la renta que desea devolver (o 0 para cancelar)").strip()

    if id_renta == "0":
        console.print("\n[bold yellow]⚠️ Operación cancelada.[/bold yellow]")
        funciones.espereTecla()
        return

    renta_seleccionada = None
    for r in rentas_activas:
        if str(r['id']) == id_renta:
            renta_seleccionada = r
            break

    # Actualizar estado a devuelto
    with console.status("[bold green]Procesando devolución...", spinner="dots"):
        exito = rentas_crud.actualizar_estado(renta_seleccionada['id'], funciones.ESTADO_DEVUELTO, conexionBD)
        time.sleep(0.5)

    if exito:
        libro = libros_crud.buscar_por_id(renta_seleccionada['id_libro'], conexionBD)
        if libro is not None:
            nuevo_stock = libro['stock'] + 1
            libros_crud.actualizar_stock(renta_seleccionada['id_libro'], nuevo_stock, conexionBD)
        
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()


# Opciones para administradores
def ver_rentas_generales(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: MONITOREO GENERAL DE RENTAS (ADMIN) :::.......[/bold yellow]\n")

    console.print("  [bold cyan]1)[/bold cyan] Ver solo rentas ACTIVAS")
    console.print("  [bold cyan]2)[/bold cyan] Ver HISTORIAL COMPLETO de rentas\n")
    
    opc = Prompt.ask("👉 Seleccione una opción").strip()

    with console.status("[bold yellow]Consultando registros...", spinner="dots"):
        if opc == "1":
            lista = rentas_crud.consultar_todas_activas(conexionBD)
            titulo_seccion = "RENTAS ACTIVAS ACTUALMENTE"
        else:
            lista = rentas_crud.consultar_historial_general(conexionBD)
            titulo_seccion = "HISTORIAL GENERAL DE RENTAS"
        time.sleep(0.4)

    funciones.borrarPantalla()
    console.print(f"[bold yellow].......:::: {titulo_seccion} :::.......[/bold yellow]\n")

    if len(lista) > 0:
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Cliente", style="bold white")
        tabla.add_column("Libro", style="white")
        tabla.add_column("Fecha Renta", justify="center", style="yellow")
        tabla.add_column("Fecha Dev.", justify="center", style="yellow")
        tabla.add_column("Estado", justify="center")

        for r in lista:
            estado_style = "[bold green]ACTIVA[/bold green]" if r['estado'] == funciones.ESTADO_ACTIVO else "[dim]DEVUELTO[/dim]"
            tabla.add_row(str(r['id']), r['cliente'], r['libro'], str(r['fecha_renta']), str(r['fecha_devolucion']), estado_style)

        console.print(tabla)
    else:
        console.print("[bold yellow]⚠️ No hay registros disponibles para mostrar.[/bold yellow]")

    funciones.espereTecla()


def devolver_libro_admin(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold yellow].......:::: PROCESAR DEVOLUCIÓN DE LIBRO (ADMIN) :::.......[/bold yellow]\n")

    with console.status("[bold yellow]Consultando préstamos activos...", spinner="dots"):
        rentas_activas = rentas_crud.consultar_todas_activas(conexionBD)
        time.sleep(0.4)

    if len(rentas_activas) == 0:
        console.print("[bold green]✨ No hay libros pendientes por devolver en el sistema.[/bold green]")
        funciones.espereTecla()
        return

    tabla = Table(header_style="bold magenta", border_style="cyan")
    tabla.add_column("ID Renta", justify="center", style="cyan")
    tabla.add_column("Cliente", style="bold white")
    tabla.add_column("Libro", style="white")
    tabla.add_column("Fecha Dev.", justify="center", style="yellow")

    for r in rentas_activas:
        tabla.add_row(str(r['id']), r['cliente'], r['libro'], str(r['fecha_devolucion']))

    console.print(tabla)

    ids_validos = [str(r['id']) for r in rentas_activas]
    id_renta = Prompt.ask("\n🎯 Ingrese el ID de la renta a recibir (o 0 para cancelar)").strip()

    while id_renta != "0" and id_renta not in ids_validos:
        funciones.opcionInvalida()
        id_renta = Prompt.ask("🎯 Ingrese el ID de la renta a recibir (o 0 para cancelar)").strip()

    if id_renta == "0":
        console.print("\n[bold yellow]⚠️ Operación cancelada.[/bold yellow]")
        funciones.espereTecla()
        return

    renta_sel = None
    for r in rentas_activas:
        if str(r['id']) == id_renta:
            renta_sel = r
            break

    # Marcar como devuelto en la base de datos
    with console.status("[bold green]Registrando devolución en el sistema...", spinner="dots"):
        exito = rentas_crud.actualizar_estado(renta_sel['id'], funciones.ESTADO_DEVUELTO, conexionBD)
        time.sleep(0.5)

    if exito:
        libro = libros_crud.buscar_por_id(renta_sel['id_libro'], conexionBD)
        if libro is not None:
            nuevo_stock = libro['stock'] + 1
            libros_crud.actualizar_stock(renta_sel['id_libro'], nuevo_stock, conexionBD)
        
        console.print(f"\n[bold green]✅ Se recibió con éxito el libro '{renta_sel['libro']}' devuelto por {renta_sel['cliente']}.[/bold green]")
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()