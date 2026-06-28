from textual.screen import Screen
from textual.widgets import Static
from textual.containers import Vertical
from textual.app import ComposeResult
from rich.text import Text
from rich.panel import Panel
from rich import box

from gameLogic.dbUtils import wordDB
from styles import gruvbox

# Debug Stuff
import logging

log = logging.getLogger("resultsScreen")


def fetch_definition(word):
    definition = wordDB.getWordDefinition(word)
    return definition


class WinScreen(Screen):
    CSS_PATH = "../styles/results.tcss"

    def __init__(
        self, word, stageScore, totalScore, difficulty, stageNumber, definition
    ):
        super().__init__()
        self.word = word
        self.stageScore = stageScore
        self.totalScore = totalScore
        self.difficulty = difficulty
        self.stageNumber = stageNumber
        self.definition = definition

    def compose(self) -> ComposeResult:
        # apply styling
        if self.stageNumber < 3:
            yield Vertical(
                Static(
                    Text(
                        f"Congrats! You completed Stage {self.stageNumber}!\n",
                        style=f"bold {gruvbox.brightgreen}",
                    )
                ),
                Static(
                    Text(
                        f"The word was: {self.word.upper()}\n",
                        style=f"bold {gruvbox.brightpurple}",
                    )
                ),
                Static(
                    Text(
                        f"Definition: {self.definition}\n",
                        style=f"bold {gruvbox.neutralpurple}",
                    ),
                    id="definition",
                ),
                Static(
                    Text(
                        f"Stage Score: {self.stageScore}      Total Score: {self.totalScore}\n",
                        style=f"bold {gruvbox.brightblue}",
                    )
                ),
                Static(
                    Text(
                        "Press any key to continue...",
                        style=f"bold {gruvbox.brightyellow}",
                    )
                ),
                id="winScreen",
            )
        else:
            yield Vertical(
                Static(
                    Text(
                        f"Congrats! You completed all stages!\n",
                        style=f"bold {gruvbox.brightgreen}",
                    )
                ),
                Static(
                    Text(
                        f"The word was: {self.word.upper()}\n",
                        style=f"bold {gruvbox.brightpurple}",
                    )
                ),
                Static(
                    Text(
                        f"Definition: {self.definition}\n",
                        style=f"bold {gruvbox.neutralpurple}",
                    ),
                    id="definition",
                ),
                Static(
                    Text(
                        f"Stage Score: {self.stageScore}      Final Score: {self.totalScore}\n",
                        style=f"bold {gruvbox.brightblue}",
                    )
                ),
                Static(
                    Text(
                        "Press any key to continue...",
                        style=f"bold {gruvbox.brightyellow}",
                    )
                ),
                id="finalWinScreen",
            )

    def on_key(self, event):
        if self.stageNumber < 3:
            self.app.stageNumber += 1
            from gameLogic import mainGame

            mainGame.initGame(self.app)
            self.app.pop_screen()
            self.app.push_screen("GameScreen")
        else:
            self.app.pop_screen()
            self.app.push_screen("NameInputScreen")


class LoseScreen(Screen):
    CSS_PATH = "../styles/results.tcss"

    def __init__(
        self, word, stageScore, totalScore, difficulty, stageNumber, definition
    ):
        super().__init__()
        self.word = word
        self.stageScore = stageScore
        self.totalScore = totalScore
        self.difficulty = difficulty
        self.stageNumber = stageNumber
        self.definition = definition

    def compose(self) -> ComposeResult:
        # apply styling
        if self.stageNumber < 3:
            yield Vertical(
                Static(
                    Text(
                        f"Good Attempt! Keep Trying!\n",
                        style=f"bold {gruvbox.brightred}",
                    )
                ),
                Static(
                    Text(
                        f"The word was: {self.word.upper()}     This was stage {self.stageNumber}\n",
                        style=f"bold {gruvbox.brightred}",
                    )
                ),
                Static(
                    Text(
                        f"Definition: {self.definition}\n",
                        style=f"bold {gruvbox.neutralpurple}",
                    ),
                    id="definition",
                ),
                Static(
                    Text(
                        f"Stage Score: {self.stageScore}      Total Score: {self.totalScore}\n",
                        style=f"bold {gruvbox.brightblue}",
                    )
                ),
                Static(
                    Text(
                        "Press any key to continue...",
                        style=f"bold {gruvbox.brightyellow}",
                    )
                ),
                id="loseScreen",
            )

        else:
            yield Vertical(
                Static(
                    Text(
                        f"Congrats! You attempted all stages!\n",
                        style=f"bold {gruvbox.brightgreen}",
                    )
                ),
                Static(
                    Text(
                        f"The word was: {self.word.upper()}\n",
                        style=f"bold {gruvbox.brightpurple}",
                    )
                ),
                Static(
                    Text(
                        f"Definition: {self.definition}\n",
                        style=f"bold {gruvbox.neutralpurple}",
                    ),
                    id="definition",
                ),
                Static(
                    Text(
                        f"Stage Score: {self.stageScore}      Final Score: {self.totalScore}\n",
                        style=f"bold {gruvbox.brightblue}",
                    )
                ),
                Static(
                    Text(
                        "Press any key to continue...",
                        style=f"bold {gruvbox.brightyellow}",
                    )
                ),
                id="finalLoseScreen",
            )

    def on_key(self, event):
        if self.stageNumber < 3:
            log.info(f"[ResultScreen.on_key BEFORE initGame] word={self.app.word}")
            self.app.stageNumber += 1
            from gameLogic import mainGame

            mainGame.initGame(self.app)
            log.info(f"[ResultScreen.on_key AFTER initGame] word={self.app.word}")
            log.info(f"[ResultScreen.on_key] popping result screen")
            self.app.pop_screen()
            log.info(f"[ResultScreen.on_key] pushing GameScreen")
            self.app.push_screen("GameScreen")
        else:
            self.app.pop_screen()
            self.app.push_screen("NameInputScreen")
