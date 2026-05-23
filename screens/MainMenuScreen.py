from textual.screen import Screen
from textual.widgets import Static, Input
from textual.containers import Horizontal, Vertical
from textual.app import ComposeResult

from styles import displayPixelArt
from menuLogic import mainMenu, difficultySelection


class MainMenuScreen(Screen):
    CSS_PATH = "../styles/mainmenu.tcss"
    currentScreen = "menu"

    def __init__(self):
        super().__init__()
        self.mode = "menu"  # "menu", "difficultyForGame", "difficultyForHighScores"
        self.highscores_mode = False

    def compose(self) -> ComposeResult:
        yield Static(displayPixelArt.printLogoCenteredBoxed(), id="logo")
        with Horizontal():
            yield Static(mainMenu.buildMenuPanel(), id="menu")
            with Vertical(id="input-box"):
                yield Static("[bold underline]Input[/bold underline]", id="input")
                yield Static("Select an option from the list.", id="wrapped-text")
                yield Input(
                    placeholder="1, 2 or 3:",
                    type="integer",
                    restrict=r"[1234]",
                    id="menuInput",
                )

    def on_input_submitted(self, event):
        if event.input.id == "menuInput":
            if self.currentScreen == "menu" and event.value == "3":
                self.notify("Thanks for Playing!!")
                self.set_timer(1, self.app.exit)

            elif self.currentScreen == "menu" and (
                event.value == "1" or event.value == "2"
            ):
                mainMenu.menuInputs(event.value, self)
            elif self.currentScreen == "difficultySelection":
                difficultySelection.difficultyInputs(event.value, self)

            self.query_one("#menuInput", Input).clear()

    def on_screen_resume(self):
        if self.currentScreen == "difficultySelection":
            self.query_one("#menu").update(difficultySelection.buildDifficultyPanel())
        elif self.currentScreen == "menu":
            self.query_one("#menu").update(mainMenu.buildMenuPanel())
        self.query_one("#menuInput", Input).clear()
