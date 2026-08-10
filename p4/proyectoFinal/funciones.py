import re
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
import time
from rich.text import Text

# Objeto Console global para usar en todo el proyecto
console = Console()

# CONSTANTES DEL SISTEMA 
DIAS_PRESTAMO_ESTUDIANTE = 15
DIAS_PRESTAMO_GENERAL = 7

ESTADO_ACTIVO = "ACTIVA"
ESTADO_DEVUELTO = "DEVUELTO"


def borrarPantalla():
    console.clear()


def espereTecla():
    Prompt.ask("\n[bold blue]✨ ...¡Oprima cualquier tecla para continuar!...[/bold blue]", default="", show_default=False)


def accionExitosa():
    console.print("\n[bold green]✅ ...¡Acción Realizada con Éxito!...[/bold green]")
    Prompt.ask("\n[dim]Presiona Enter para continuar[/dim]", default="", show_default=False)
    borrarPantalla()


def accionNOExitosa():
    console.print("\n[bold red]❌ ...¡No fue posible realizar esta Acción, inténtalo nuevamente!...[/bold red]")
    Prompt.ask("\n[dim]Presiona Enter para continuar[/dim]", default="", show_default=False)
    borrarPantalla()


def terminarSistema():
    mensaje = Align.center(
        "[bold cyan]🚀 GRACIAS POR UTILIZAR NUESTRO SISTEMA 🚀[/bold cyan]\n\n"
        "[italic white]¡Vuelve pronto![/italic white]"
    )
    console.print(Panel(mensaje, border_style="bright_magenta", expand=False))
    Prompt.ask("\n[dim]Presiona Enter para salir[/dim]", default="", show_default=False)


def opcionInvalida():
    console.print("\n[bold red]⚠️ .... ¡Opción inválida, vuelve a intentarlo!....[/bold red]")
    Prompt.ask("\n[dim]Presiona Enter para continuar[/dim]", default="", show_default=False)


def validarCorreo(correo):
    """
    Usa RegEx para comprobar que el correo tenga la estructura:
    texto + @ + texto + . + texto (Ejemplo: usuario@dominio.com)
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    return False


def menuSecundario():
    console.print("[bold blue].......:::: A C C I O N E S ::::.......[/bold blue]\n")
    console.print("  [bold cyan]1)[/bold cyan] ➕ Agregar")
    console.print("  [bold cyan]2)[/bold cyan] 🗑️ Borrar")
    console.print("  [bold cyan]3)[/bold cyan] ✏️ Modificar")
    console.print("  [bold cyan]4)[/bold cyan] 📋 Mostrar")
    console.print("  [bold cyan]5)[/bold cyan] 🔍 Buscar")
    console.print("  [bold cyan]6)[/bold cyan] 🧹 Limpiar")
    console.print("  [bold red]7)[/bold red] ↩️ Regresar\n")
    
    opcion = Prompt.ask("👉 Elige una opción").strip()
    return opcion


def cancelarOperacion(valor):
    if valor == "0":
        console.print("\n[bold orange]⚠️ Operación cancelada por el usuario.[/bold orange]")
        espereTecla()
        return True
    return False

console = Console()

def bienvenida_creativa():
    borrarPantalla()
    
    # 1. Animación de carga y verificación de componentes
    pasos_arranque = [
        "Iniciando componentes del sistema...",
        "Estableciendo conexión segura con MySQL...",
        "Cargando paquetes (Usuarios, Libros, Rentas)...",
        "Verificando constantes y archivos del sistema...",
        "¡Inicialización completada con éxito!"
    ]
    
    for paso in pasos_arranque:
        with console.status(f"[bold cyan]{paso}[/bold cyan]", spinner="dots"):
            time.sleep(0.8)
            
    console.print()
    
    # 2. Banner de Bienvenida
    contenido = Text(
        "📖 B I E N V E N I D O   A L   S I S T E M A 📖\n\n"
        "Plataforma de Control de Catálogo, Usuarios y Préstamos",
        justify="center",
        style="bold bright_white"
    )
    
    panel_bienvenida = Panel(
        Align.center(contenido),
        title="[bold green]● SISTEMA EN LÍNEA ●[/bold green]",
        border_style="bright_blue",
        padding=(1,8)
    )
    
    console.print(panel_bienvenida)
    time.sleep(2.2)

def despedida_creativa():
    borrarPantalla()
    
    # 1. Animación de cierre de conexiones
    pasos_cierre = [
        "Guardando sesión de usuario...",
        "Cerrando conexiones activas con MySQL...",
        "Verificando integridad de datos y archivos TXT...",
        "¡Sistema finalizado con éxito!"
    ]
    
    for paso in pasos_cierre:
        with console.status(f"[bold cyan]{paso}[/bold cyan]", spinner="dots"):
            time.sleep(1)
            
    console.print()
    
    # 2. Dos frases escritas una tras otra
    frases = [
        "«Un hogar sin libros es como un cuerpo sin alma.» — Cicerón",
        "«La educación es el arma más poderosa que puedes usar para cambiar el mundo.» — Nelson Mandela"
    ]
    
    for frase in frases:
        console.print("\t[italic yellow]", end="")
        for letra in frase:
            print(letra, end="", flush=True)
            time.sleep(0.025)
        console.print("\n")
        time.sleep(0.3)

    # 3. Banner final de despedida
    contenido = Text(
        "📚 ¡Gracias por utilizar nuestro sistema! 📚\n\n"
        "Que tengas un excelente día. ¡Esperamos verte pronto!",
        justify="center",
        style="bold bright_white"
    )
    
    panel_despedida = Panel(
        Align.center(contenido),
        title="[bold green]● SISTEMA APAGADO ●[/bold green]",
        border_style="bright_blue",
        padding=(1, 4)
    )
    
    console.print(panel_despedida)
    time.sleep(1.8)