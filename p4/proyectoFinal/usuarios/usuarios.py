import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import funciones
from usuarios import crud

console = Console()

def agregar(conexionBD, es_publico=False):
    console.print("[bold cyan].......:::: AGREGAR USUARIO ::::.......[/bold cyan]\n")

    nombre = Prompt.ask("👤 Ingrese nombre completo (o 0 para cancelar)").upper().strip()
    if funciones.cancelarOperacion(nombre):
        return

    # validación de correo con RegEx
    correo_valido = False
    correo = ""
    while not correo_valido:
        correo = Prompt.ask("📧 Ingrese correo electrónico (o 0 para cancelar)").strip()
        if funciones.cancelarOperacion(correo):
            return

        if funciones.validarCorreo(correo):
            correo_valido = True
        else:
            console.print("[bold red]⚠️ Formato de correo no válido. Ejemplo: usuario@gmail.com[/bold red]\n")
            funciones.espereTecla()
    
    # ASIGNACIÓN DE ROL SEGÚN EL TIPO DE REGISTRO
    if es_publico:
        rol = "USUARIO"  # Si viene del registro público, es USUARIO automáticamente
    else:
        # Si lo registra un empleado, pide y valida el rol normalmente
        rol = Prompt.ask("🛡️ Ingrese su rol (Empleado o Usuario)").upper().strip()
        if funciones.cancelarOperacion(rol):
            return
        while rol != "EMPLEADO" and rol != "USUARIO":
            console.print("[bold red]⚠️ Opción no válida, ingresa solo una de las opciones disponibles (Empleado o Usuario)[/bold red]")
            funciones.espereTecla()
            funciones.borrarPantalla()
            rol = Prompt.ask("🛡️ Ingrese su rol (Empleado o Usuario)").upper().strip()

    estudiante = Prompt.ask("🎓 ¿Es estudiante? (Si/No)").upper().strip()
    if funciones.cancelarOperacion(estudiante):
        return
    while estudiante != "SI" and estudiante != "NO":
        console.print("[bold red]⚠️ Opción no válida, ingresa solo una de las opciones disponibles (Si/No)[/bold red]")
        funciones.espereTecla()
        funciones.borrarPantalla()
        estudiante = Prompt.ask("🎓 ¿Es estudiante? (Si/No)").upper().strip()

    with console.status("[bold green]Guardando usuario en el sistema...", spinner="dots"):
        respuesta = crud.insertar(nombre, correo, rol, estudiante, conexionBD)
        time.sleep(1.4)

    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()


def mostrarUsuarios(conexionBD):
    console.print("[bold yellow].......:::: MOSTRAR USUARIOS ::::.......[/bold yellow]\n")
    
    # Consultar en la base de datos con efecto visual de carga
    with console.status("[bold yellow]Consultando base de datos...", spinner="dots"):
        usuarios = crud.consultar(conexionBD)
        time.sleep(1)

    if len(usuarios) > 0:
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Nombre", style="bold white")
        tabla.add_column("Correo", style="yellow")
        tabla.add_column("Rol", justify="center")
        tabla.add_column("Estudiante", justify="center")

        for u in usuarios:
            rol_style = "[bold green]EMPLEADO[/bold green]" if u['rol'] == "EMPLEADO" else "[cyan]USUARIO[/cyan]"
            est_style = "[bold green]SI[/bold green]" if u['estudiante'] == "SI" else "[dim]NO[/dim]"
            tabla.add_row(str(u['id']), u['nombre'], u['correo'], rol_style, est_style)

        console.print(tabla)
    else:
        console.print("[bold yellow]⚠️ No hay usuarios actualmente para mostrar[/bold yellow]")

    funciones.espereTecla()


def limpiarUsuarios(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold red].......:::: VACIAR REGISTRO DE USUARIOS ::::.......[/bold red]\n")

    console.print("[bold red]⚠️ ADVERTENCIA:[/bold red] Esta acción borrará a [bold red]TODOS[/bold red] los usuarios registrados.")
    console.print("[dim]Se preservará únicamente la cuenta del Administrador Principal por defecto.[/dim]\n")

    opc = Prompt.ask("¿Desea continuar con el vaciado? (Si/No)").lower().strip()

    while opc not in ["si", "no"]:
        funciones.opcionInvalida()
        opc = Prompt.ask("¿Desea continuar con el vaciado? (Si/No)").lower().strip()

    if opc == "si":
        with console.status("[bold red]Eliminando usuarios secundarios...", spinner="bouncingBar"):
            respuesta = crud.vaciar(conexionBD)
            time.sleep(1.6)

        if respuesta:
            funciones.borrarPantalla()
            console.print("[bold green].......:::: OPERACIÓN EXITOSA ::::.......[/bold green]\n")
            console.print("  [bold green]✅ Se han eliminado los usuarios secundarios.[/bold green]")
            console.print("  [bold cyan]📌 Se restableció la cuenta maestra:[/bold cyan]")
            console.print("     • [bold white]Nombre:[/bold white] ADMINISTRADOR GENERAL")
            console.print("     • [bold white]Correo:[/bold white] admin@gmail.com")
            console.print("     • [bold white]Rol:[/bold white] EMPLEADO")
            funciones.espereTecla()
        else:
            funciones.accionNOExitosa()
    else:
        console.print("\n[bold yellow]⚠️ Operación cancelada.[/bold yellow]")
        funciones.espereTecla()


def buscarUsuarios(conexionBD):
    console.print("[bold green].......:::: BUSCAR USUARIOS ::::.......[/bold green]\n")
    console.print("  [bold cyan]1)[/bold cyan] Buscar por nombre")
    console.print("  [bold cyan]2)[/bold cyan] Buscar por rol")
    console.print("  [bold red]3)[/bold red] Regresar\n")
    
    opcion = Prompt.ask("👉 ¿Por qué método desea hacer la búsqueda?").strip()
    resultados = []

    while opcion not in ["1", "2", "3"]:
        funciones.opcionInvalida()
        funciones.espereTecla()
        opcion = Prompt.ask("👉 ¿Por qué método desea hacer la búsqueda?").strip()

    if opcion == "1":
        funciones.borrarPantalla()
        console.print("[bold green].......:::: BUSCAR USUARIOS POR NOMBRE ::::.......[/bold green]\n")
        nombre = Prompt.ask("👤 Ingresa el nombre").upper().strip()
        with console.status("[bold yellow]Buscando coincidencias...", spinner="dots"):
            resultados = crud.buscar_por_nombre(nombre, conexionBD)
            time.sleep(1.2)

    elif opcion == "2":
        funciones.borrarPantalla()
        console.print("[bold green].......:::: BUSCAR USUARIOS POR ROL ::::.......[/bold green]\n")
        rol = Prompt.ask("🛡️ Ingresa el rol").upper().strip()
        with console.status("[bold yellow]Buscando coincidencias...", spinner="dots"):
            resultados = crud.buscar_por_rol(rol, conexionBD)
            time.sleep(0.4)

    elif opcion == "3":
        funciones.borrarPantalla()
        return

    else:
        funciones.opcionInvalida()
        funciones.espereTecla()
        return

    if len(resultados) > 0:
        funciones.borrarPantalla()
        console.print("[bold green].......:::: RESULTADOS ENCONTRADOS ::::.......[/bold green]\n")
        
        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Nombre", style="bold white")
        tabla.add_column("Correo", style="yellow")
        tabla.add_column("Rol", justify="center")
        tabla.add_column("Estudiante", justify="center")

        for u in resultados:
            rol_style = "[bold green]EMPLEADO[/bold green]" if u['rol'] == "EMPLEADO" else "[cyan]USUARIO[/cyan]"
            est_style = "[bold green]SI[/bold green]" if u['estudiante'] == "SI" else "[dim]NO[/dim]"
            tabla.add_row(str(u['id']), u['nombre'], u['correo'], rol_style, est_style)

        console.print(tabla)
    else:
        console.print("\n[bold red]⚠️ No se encontraron usuarios con ese criterio de búsqueda.[/bold red]")

    funciones.espereTecla()


def borrarUsuario(conexionBD):
    funciones.borrarPantalla()
    console.print("[bold red].......:::: ELIMINAR USUARIO ::::.......[/bold red]\n")

    busqueda = Prompt.ask("🔍 Ingrese el nombre o coincidencia del usuario a borrar").upper().strip()

    # 1. Buscamos todas las coincidencias en la BD
    with console.status("[bold yellow]Buscando usuarios...", spinner="dots"):
        usuarios = crud.buscar_por_nombre(busqueda, conexionBD)
        time.sleep(0.4)

    if len(usuarios) == 0:
        console.print("\n[bold yellow]⚠️ No se encontraron usuarios con ese criterio de búsqueda.[/bold yellow]")
        funciones.espereTecla()
        return

    # 2. Mostramos los usuarios encontrados
    tabla = Table(header_style="bold magenta", border_style="cyan")
    tabla.add_column("ID", justify="center", style="cyan")
    tabla.add_column("Nombre", style="bold white")
    tabla.add_column("Correo", style="yellow")
    tabla.add_column("Rol", justify="center")

    for u in usuarios:
        rol_style = "[bold green]EMPLEADO[/bold green]" if u['rol'] == "EMPLEADO" else "[cyan]USUARIO[/cyan]"
        tabla.add_row(str(u['id']), u['nombre'], u['correo'], rol_style)

    console.print(tabla)

    # Creamos una lista con los IDs permitidos (en texto) para validar rápidamente
    ids_validos = [str(u['id']) for u in usuarios]

    # 3. BUCLE 1: Validación del ID seleccionado
    id_borrar = Prompt.ask("\n🎯 Ingrese el ID del usuario que desea eliminar (o 0 para cancelar)").strip()

    while id_borrar != "0" and id_borrar not in ids_validos:
        console.print("[bold red]⚠️ ID no válido o no se encuentra en la lista mostrada. Intente de nuevo.[/bold red]")
        id_borrar = Prompt.ask("🎯 Ingrese el ID del usuario a eliminar (o 0 para cancelar)").strip()

    # Si seleccionó 0, cancelamos
    if id_borrar == "0":
        console.print("\n[bold green]⚠️ Operación cancelada.[/bold green]")
        funciones.espereTecla()
        return

    # Extraemos el usuario seleccionado
    usuario_seleccionado = None
    for u in usuarios:
        if str(u['id']) == id_borrar:
            usuario_seleccionado = u
            break

    # 4. BUCLE 2: Validación de la confirmación (Si/No)
    confirmacion = Prompt.ask(
        f"\n❓ ¿Está seguro que desea eliminar a [bold white]{usuario_seleccionado['nombre']}[/bold white] (ID: {usuario_seleccionado['id']})? (Si/No)"
    ).lower().strip()

    while confirmacion not in ["si", "no"]:
        funciones.opcionInvalida()
        confirmacion = Prompt.ask(
            f"❓ ¿Está seguro que desea eliminar a [bold white]{usuario_seleccionado['nombre']}[/bold white] (ID: {usuario_seleccionado['id']})? (Si/No)"
        ).lower().strip()

    # 5. Ejecutamos la acción según la respuesta validada
    if confirmacion == "si":
        with console.status("[bold red]Eliminando usuario de la base de datos...", spinner="bouncingBar"):
            respuesta = crud.borrar(usuario_seleccionado['id'], conexionBD)
            time.sleep(0.5)

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        console.print("\n[bold yellow]⚠️ Eliminación cancelada.[/bold yellow]")
        funciones.espereTecla()


def modificarUsuario(conexionBD):
    while True:
        funciones.borrarPantalla()
        console.print("[bold green].......:::: MODIFICAR USUARIO ::::.......[/bold green]\n") 

        # 1. Obtenemos y mostramos la lista completa al inicio
        with console.status("[bold yellow]Cargando lista de usuarios...", spinner="dots"):
            todos_usuarios = crud.consultar(conexionBD)
            time.sleep(0.3)

        if not todos_usuarios:
            console.print("[bold red]⚠️ No hay usuarios registrados en el sistema.[/bold red]")
            funciones.espereTecla()
            return

        tabla = Table(header_style="bold magenta", border_style="cyan")
        tabla.add_column("ID", justify="center", style="cyan")
        tabla.add_column("Nombre", style="bold white")
        tabla.add_column("Correo", style="yellow")
        tabla.add_column("Rol", justify="center")
        tabla.add_column("Estudiante", justify="center")

        for u in todos_usuarios:
            rol_style = "[bold green]EMPLEADO[/bold green]" if u['rol'] == "EMPLEADO" else "[cyan]USUARIO[/cyan]"
            est_style = "[bold green]SI[/bold green]" if u['estudiante'] == "SI" else "[dim]NO[/dim]"
            tabla.add_row(str(u['id']), u['nombre'], u['correo'], rol_style, est_style)

        console.print(tabla)
        console.print()

        # 2. Pedimos el nombre del usuario a modificar
        nombre_ingresado = Prompt.ask("🔍 Escribe el nombre del usuario a modificar (o 0 para cancelar)").strip().upper()

        if nombre_ingresado == "0":
            console.print("\n[bold yellow]⚠️ Operación cancelada.[/bold yellow]")
            funciones.espereTecla()
            return

        #VALIDACIÓN INMEDIATA EN BÚSQUEDA
        if not nombre_ingresado:
            funciones.opcionInvalida()
            funciones.espereTecla()
            continue

        # Buscamos en la BD inmediatamente
        usuarios_encontrados = crud.buscar_por_nombre(nombre_ingresado, conexionBD)

        # Si NO existe coincidencia, cortamos AQUÍ MISMO y avisamos
        if not usuarios_encontrados or len(usuarios_encontrados) == 0:
            console.print(f"\n[bold red]⚠️ Error: No existe ningún usuario con el nombre '{nombre_ingresado}'.[/bold red]")
            funciones.opcionInvalida()
            funciones.espereTecla()
            continue  # Recarga la lista para que intente de nuevo

        #Guardamos el NOMBRE EXACTO guardado en la BD
        nombre_exacto_bd = usuarios_encontrados[0]['nombre']

        # 3. Preguntar si realmente desea modificarlo
        opc = Prompt.ask(f"\n❓ ¿Deseas modificar a '[bold white]{nombre_exacto_bd}[/bold white]'? (Si/No)").strip().lower()
        while opc not in ["si", "no"]:
            funciones.opcionInvalida()
            funciones.espereTecla()
            opc = Prompt.ask(f"❓ ¿Deseas modificar a '{nombre_exacto_bd}'? (Si/No)").strip().lower()

        if opc == "no":
            console.print("\n[bold yellow][-] Operación cancelada.[/bold yellow]")
            funciones.espereTecla()
            return

        # 4. SOLO HASTA AQUÍ PEDIMOS LOS NUEVOS DATOS (Porque ya confirmamos que el usuario existe)
        funciones.borrarPantalla()
        console.print(f"\n[bold cyan]--- INGRESANDO NUEVOS DATOS PARA: {nombre_exacto_bd} ---[/bold cyan]\n")
        
        nombre_new = Prompt.ask("👤 Ingresa el nuevo nombre completo").strip().upper()

        # Validación de Correo
        correo_valido = False
        correo = ""
        while not correo_valido:
            correo = Prompt.ask("📧 Ingresa el nuevo correo electrónico").strip()
            if funciones.validarCorreo(correo):
                correo_valido = True
            else:
                console.print("[bold red]⚠️ Formato de correo no válido. Ejemplo: usuario@gmail.com[/bold red]\n")
                funciones.espereTecla()

        # Validación de Rol
        rol = Prompt.ask("🛡️ Ingresa el nuevo rol (Empleado o Usuario)").strip().upper()
        while rol not in ["EMPLEADO", "USUARIO"]:
            funciones.opcionInvalida()
            funciones.espereTecla()
            rol = Prompt.ask("🛡️ Ingresa el nuevo rol (Empleado o Usuario)").strip().upper()

        # Validación de Estudiante
        estudiante = Prompt.ask("🎓 ¿Es estudiante? (Si/No)").strip().upper()
        while estudiante not in ["SI", "NO"]:
            funciones.opcionInvalida()
            funciones.espereTecla()
            estudiante = Prompt.ask("🎓 ¿Es estudiante? (Si/No)").strip().upper()

        # 5. Enviamos a actualizar pasando 'nombre_exacto_bd'
        with console.status("[bold green]Actualizando información en BD...", spinner="dots"):
            respuesta = crud.actualizar(nombre_new, correo, rol, estudiante, nombre_exacto_bd, conexionBD)
            time.sleep(1.2)

        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()

        break