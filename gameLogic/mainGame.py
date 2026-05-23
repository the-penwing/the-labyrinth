# import external libs
from rich.text import Text
from rich.console import Group
from rich_pixels import Pixels

# import custom modules
from gameLogic.dbUtils import wordDB
from styles import gruvbox

db = wordDB("data/words.db")


def initGame(app):
    app.app.word = db.getRandomWord(app.app.word_length)
    app.app.remainingGuesses = 15
    app.app.correctGuesses = 0
    app.app.incorrectGuesses = 0
    app.app.guessedLetters = []
    app.app.scoreValid = True


def createWordDisplay(word, guessedLetters):
    displayedLetters = []
    for letter in word:
        if letter in guessedLetters:
            displayedLetters.append(letter.upper())
        else:
            displayedLetters.append("_")
    return " ".join(displayedLetters)


def checkGuess(app, word, guess):
    guess = guess.lower()
    app.guessedLetters.append(guess)
    if guess not in word:
        app.incorrectGuesses = app.incorrectGuesses + 1
        app.remainingGuesses = app.remainingGuesses - 1
    else:
        app.correctGuesses = app.correctGuesses + 1


def checkVictory(app):
    if app.remainingGuesses > 0:
        for letter in app.word:
            if letter not in app.guessedLetters:
                return False
        return True
    else:
        return False


def createAlphabetDisplay(word, guessedLetters):
    t = Text(justify="center")
    t.append("Alphabet\n", style=f"bold underline {gruvbox.neutralaqua}")

    alphabet = Text(justify="center")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter in guessedLetters:
            if letter in word:
                alphabet.append(
                    letter.upper() + " ", style=f"bold {gruvbox.brightgreen}"
                )
            else:
                alphabet.append(letter.upper() + " ", style=f"bold {gruvbox.brightred}")
        else:
            alphabet.append(letter.upper() + " ", style=f"dim {gruvbox.light4}")
    t.append(alphabet)
    return t


def createProgressGraphic(remainingGuesses):
    progress = Text(justify="center")
    for i in range(15):
        if i < remainingGuesses:
            progress.append("● ", style=f"{gruvbox.brightgreen}")
        else:
            progress.append("○ ", style=f"{gruvbox.brightred}")
    return progress
