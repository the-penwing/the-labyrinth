import logging
from textual.screen import Screen
from textual.widgets import Static, Input
from textual.containers import Horizontal, Vertical
from textual.app import ComposeResult

from gameLogic import mainGame
from gameLogic.calculateScore import totalPoints, findScore
from screens.ResultsScreen import WinScreen, LoseScreen, fetch_definition

log = logging.getLogger("GameScreen")


class GameScreen(Screen):
    CSS_PATH = "../styles/gamescreen.tcss"

    def on_mount(self):
        log.info(
            f"[GameScreen.on_mount] word={self.app.word}, guessed={self.app.guessedLetters}"
        )  # type: ignore

    def compose(self) -> ComposeResult:
        log.info(
            f"[GameScreen.compose] word={self.app.word}, guessed={self.app.guessedLetters}"
        )  # type: ignore
        with Horizontal():
            with Vertical():  # left panel
                yield Static(
                    mainGame.createWordDisplay(self.app.word, self.app.guessedLetters),  # type: ignore
                    id="word-progress",
                )
                yield Static(
                    mainGame.createAlphabetDisplay(
                        self.app.word, self.app.guessedLetters
                    ),
                    id="alphabet",
                )  # type: ignore
            with Vertical():  # right panel
                with Horizontal():  # top
                    yield Static(
                        f"You have {self.app.remainingGuesses} guess(es) remaining",  # type: ignore
                        id="guess-counter",
                    )
                    yield Static(
                        mainGame.createProgressGraphic(self.app.remainingGuesses),
                        id="progress-graphic",
                    )  # type: ignore
                yield Input(
                    placeholder="Enter a Letter",
                    type="text",
                    restrict=r"[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]",
                    id="game-input-box",
                )

    def on_input_submitted(self, event):

        # self.notify(f"{self.app.word}")  # type: ignore
        # Notifys the player of the word for testing purposes, can be enabled for debugging but should be disabled for actual gameplay
        if event.input.id == "game-input-box":
            if event.value in self.app.guessedLetters:  # type: ignore
                self.query_one("#game-input-box", Input).clear()
                self.query_one("#game-input-box", Input).focus()
                self.notify(
                    f"You have already guessed {event.value}, Please make a different guess"
                )
            else:
                mainGame.checkGuess(self.app, self.app.word, event.value)  # type: ignore
                self.query_one("#game-input-box", Input).clear()
                self.query_one("#game-input-box", Input).focus()
                self.query_one("#word-progress", Static).update(
                    mainGame.createWordDisplay(self.app.word, self.app.guessedLetters)  # type: ignore
                )
                self.query_one("#alphabet", Static).update(
                    mainGame.createAlphabetDisplay(
                        self.app.word, self.app.guessedLetters
                    )  # type: ignore
                )
                self.query_one("#guess-counter", Static).update(
                    f"You have {self.app.remainingGuesses} guess(es) remaining"  # type: ignore
                )
                self.query_one("#progress-graphic", Static).update(
                    mainGame.createProgressGraphic(self.app.remainingGuesses)  # type: ignore
                )
                hasWon = mainGame.checkVictory(self.app)
                if hasWon:
                    points = totalPoints(
                        self.app.correctGuesses, self.app.incorrectGuesses
                    )  # type: ignore
                    roundScore = findScore(self.app.remainingGuesses, points)  # type: ignore
                    self.app.totalScore += roundScore  # type: ignore
                    self.app.stageScore.append(roundScore)  # type: ignore
                    definition = fetch_definition(self.app.word)  # type: ignore
                    self.app.push_screen(
                        WinScreen(
                            self.app.word,
                            roundScore,
                            self.app.totalScore,
                            self.app.difficulty,
                            self.app.stageNumber,
                            definition,
                        )
                    )  # type: ignore
                elif self.app.remainingGuesses == 0:  # type: ignore
                    points = totalPoints(
                        self.app.correctGuesses, self.app.incorrectGuesses
                    )  # type: ignore
                    roundScore = findScore(self.app.remainingGuesses, points)  # type: ignore
                    self.app.totalScore += roundScore  # type: ignore
                    self.app.stageScore.append(roundScore)  # type: ignore
                    definition = fetch_definition(self.app.word)  # type: ignore
                    self.app.push_screen(
                        LoseScreen(
                            self.app.word,
                            roundScore,
                            self.app.totalScore,
                            self.app.difficulty,
                            self.app.stageNumber,
                            definition,
                        )
                    )  # type: ignore

    def on_screen_resume(self):
        self.query_one("#game-input-box", Input).clear()
        self.query_one("#game-input-box", Input).focus()
        self.query_one("#word-progress", Static).update(
            mainGame.createWordDisplay(self.app.word, self.app.guessedLetters)  # type: ignore
        )
        self.query_one("#alphabet", Static).update(
            mainGame.createAlphabetDisplay(self.app.word, self.app.guessedLetters)  # type: ignore
        )
        self.query_one("#guess-counter", Static).update(
            f"You have {self.app.remainingGuesses} guess(es) remaining"  # type: ignore
        )
        self.query_one("#progress-graphic", Static).update(
            mainGame.createProgressGraphic(self.app.remainingGuesses)  # type: ignore
        )
