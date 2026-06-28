from textual.screen import Screen
from textual.widgets import Button, Checkbox, Input
from textual.containers import Vertical, Center
from textual.app import ComposeResult


class NameInputScreen(Screen):
    CSS_PATH = "../styles/nameinputscreen.tcss"

    def compose(self) -> ComposeResult:
        self.first_name_input = Input(
            "Enter your first name: ", type="text", id="first_name"
        )
        self.last_name_or_inital_input = Input(
            "Enter your last name or last inital: ",
            type="text",
            id="last_name_or_inital",
        )
        self.anonymous_checkbox = Checkbox("Save as Anonymous?", id="anonymous_check")
        self.save_button = Center(Button("Save", id="save_button"))
        yield Vertical(
            self.first_name_input,
            self.last_name_or_inital_input,
            self.anonymous_checkbox,
            self.save_button,
            id="widget_stack",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button.id

        if button == "save_button":
            first_name = self.query_one("#first_name", Input).value
            last_name = self.query_one("#last_name_or_inital", Input).value
            is_anonymous = self.query_one("#anonymous_check", Checkbox).value

            if is_anonymous:
                first_name = "Anonymous"
                last_name = ""
            elif first_name and last_name:
                self.query_one("#first_name", Input).clear()
                self.query_one("#last_name_or_inital", Input).clear()
                self.query_one("#anonymous_check", Checkbox).value = False
            else:
                self.notify("Please fill in both names or check Anonymous")
                return

            from gameLogic.highScoresLogic.highScoresManager import HighScoresManager

            manager = HighScoresManager("data/highscores.json")
            manager.save_score(
                self.app.difficulty, first_name, last_name, self.app.totalScore
            )

            self.notify("Score Saved")
            self.app.pop_screen()
            self.app.pop_screen()
            self.app.push_screen("FinishScreen")


class FinishScreen(Screen):
    CSS_PATH = "../styles/finishscreen.tcss"

    def compose(self) -> ComposeResult:
        menu_button = Button("Play Again", id="menu_button")
        quit_button = Button("Quit", id="quit_button")
        with Vertical(id="widget_stack"):
            yield menu_button
            yield quit_button

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button.id

        if button == "menu_button":
            self.app.currentScreen = "menu"  # Reset to main menu view # type: ignore
            self.app.mode = "menu"  # Reset mode # type: ignore
            self.app.pop_screen()
            self.app.push_screen("MainMenuScreen")
        elif button == "quit_button":
            self.app.exit()
