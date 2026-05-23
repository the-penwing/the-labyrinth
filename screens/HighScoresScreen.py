from textual.screen import Screen
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal
from textual.app import ComposeResult
from rich.text import Text
from styles import gruvbox
import logging

log = logging.getLogger("debug")


class HighScoresScreen(Screen):
    CSS_PATH = "../styles/highscores.tcss"

    def get_formatted_scores(self):
        from gameLogic.highScoresLogic.highScoresManager import HighScoresManager

        manager = HighScoresManager("data/highscores.json")
        top_5 = manager.get_top_n(
            self.app.highscores_difficulty,
            5,  # type: ignore
        )  # Use app directly # type: ignore

        formatted_lines = []
        for rank, entry in enumerate(top_5, start=1):  # start=1 gives ranks 1, 2, 3...
            line = f"{rank}. {entry['firstname']} {entry['initial_or_lastname']} - {entry['score']} - {entry['date']}"
            formatted_lines.append(line)
        return "\n".join(formatted_lines)

    def compose(self) -> ComposeResult:
        title = Static(
            Text(
                f"High Scores for {self.app.highscores_difficulty.upper()} Mode",  # type: ignore
                style=f"bold {gruvbox.brightgreen}",
            ),
            id="title",
        )

        loading_scores = Static("Loading scores...", id="scores")

        buttons = Horizontal(
            Button("Menu", id="menu_button"),
            Button("Change Difficulty", id="change_difficulty_button"),
            Button("Quit", id="quit_button"),
            id="buttons_stack",
        )

        yield title
        yield loading_scores
        yield buttons

    def on_mount(self):

        log.info(f"self.app.highscores_difficulty = {self.app.highscores_difficulty}")
        difficulty = self.app.highscores_difficulty  # type: ignore
        scores_text = self.get_formatted_scores()
        log.info(f"First score line = {scores_text.split(chr(10))[0]}")
        self.query_one("#title", Static).update(
            Text(
                f"High Scores for {difficulty.upper()} Difficulty",
                style=f"bold {gruvbox.brightgreen}",
            )
        )
        self.query_one("#scores", Static).update(
            Text(scores_text, style=f"{gruvbox.brightblue}")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        if button_id == "menu_button":
            self.app.currentScreen = "menu"  # Reset to main menu view # type: ignore
            self.app.mode = "menu"  # Reset mode # type: ignore
            self.app.pop_screen()
            # Stack: [MainMenu, DifficultySelection, HighScoresScreen]
            # Pop HighScoresScreen, pop DifficultySelection = back at MainMenu
        elif button_id == "change_difficulty_button":
            self.app.currentScreen = "difficultySelection"
            self.app.mode = "difficultyForHighScores"
            self.app.pop_screen()
        elif button_id == "quit_button":
            self.app.exit()

    def on_screen_resume(self):
        self.query_one("#scores", Static).update(
            Text(self.get_formatted_scores(), style=f"{gruvbox.brightblue}")
        )
        self.query_one("#title", Static).update(
            Text(
                f"High Scores for {self.app.highscores_difficulty.upper()} Difficulty",  # type: ignore
                style=f"bold {gruvbox.brightgreen}",
            )
        )
