# import the app class that makes it all work
from textual.app import App

# import screens
from screens.MainMenuScreen import MainMenuScreen
from screens.GameScreen import GameScreen
from screens.ResultsScreen import WinScreen, LoseScreen
from screens.NameInputScreen import NameInputScreen, FinishScreen
from screens.HighScoresScreen import HighScoresScreen

# the following line is used to make my linter behave. please ignore it.
# type: ignore``


class theLabyrinth(App):
    SCREENS = {
        "MainMenuScreen": MainMenuScreen,
        "GameScreen": GameScreen,
        "HighScoresScreen": HighScoresScreen,
        "WinScreen": WinScreen,
        "LoseScreen": LoseScreen,
        "NameInputScreen": NameInputScreen,
        "FinishScreen": FinishScreen,
    }

    def on_mount(self):
        DEBUG = False  # Toggle this and uncomment a line to jump straight to a screen

        if DEBUG:
            pass
        #           self.push_screen("GameScreen")
        #           self.push_screen("WinScreen")
        #           self.push_screen("LoseScreen")
        #           self.push_screen("NameInputScreen")
        else:
            self.push_screen("MainMenuScreen")

            # initialize game state variables
            self.word = ""  # db.getRandomWord(app.difficulty)
            self.word_length = None
            self.difficulty = None
            self.remainingGuesses = 15
            self.correctGuesses = 0
            self.incorrectGuesses = 0
            self.guessedLetters = []
            self.stageNumber = 1
            self.totalScore = 0  # Track total across 3 words
            self.stageScore = []  # List of scores for each round


if __name__ == "__main__":
    theLabyrinth().run()
