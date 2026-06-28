from textual.widgets import Input
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich import box

from styles import gruvbox


def buildMenuPanel():
    t = Text(justify="center")
    t.append("MENU\n", style=f"bold underline {gruvbox.neutralaqua}")

    selections = Text(justify="left")
    selections.append("(1) Play\n")
    selections.append("(2) View High Scores\n")
    selections.append("(3) Exit\n")
    menu = Panel(
        Group(t, selections), border_style=f"{gruvbox.neutralgreen}", box=box.DOUBLE
    )
    return menu


def menuInputs(choice, app):
    from menuLogic import difficultySelection

    if choice == "1":
        app.mode = "difficultyForGame"  # Track the mode
        app.currentScreen = "difficultySelection"
        app.query_one("#menuInput", Input).placeholder = "1, 2, 3 or 4:"
        app.query_one("#menu").update(difficultySelection.buildDifficultyPanel())
    elif choice == "2":
        app.mode = "difficultyForHighScores"  # Track the mode
        app.currentScreen = "difficultySelection"
        app.query_one("#menuInput", Input).placeholder = "1, 2, 3 or 4:"
        app.query_one("#menu").update(difficultySelection.buildDifficultyPanel())
