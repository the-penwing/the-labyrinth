# import theme
from styles import gruvbox

# import from the libary rich (and rich pixels)
from rich_pixels import Pixels
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich import box

# initialising rich console
console = Console()


# function to print my logo in the center of the screen
def printLogoCentered():
    pixels = Pixels.from_image_path("assets/the-labyrinth.png")
    pixels = Align.center(pixels, vertical="middle")
    return pixels


# function to print my logo in the center of the screen, this time with a box!!
def printLogoCenteredBoxed():
    pixels = Pixels.from_image_path("assets/the-labyrinth.png")
    pixels = Align.center(pixels, vertical="middle")
    pixels = Panel(pixels, border_style=f"{gruvbox.neutralgreen}", box=box.DOUBLE)
    return pixels
