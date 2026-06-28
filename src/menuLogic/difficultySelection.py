from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich import box
import random

from styles import gruvbox
from gameLogic import mainGame

import logging

log = logging.getLogger("debug")


def buildDifficultyPanel():
    t = Text(justify="center")
    t.append("Select Difficulty\n", style=f"bold underline {gruvbox.neutralaqua}")

    selections = Text(justify="left")
    selections.append("(1) Easy\n")
    selections.append("(2) Medium\n")
    selections.append("(3) Hard\n")
    selections.append("(4) Return to Main Menu\n")
    difficultyPanel = Panel(
        Group(t, selections), border_style=f"{gruvbox.neutralgreen}", box=box.DOUBLE
    )
    return difficultyPanel


def difficultyInputs(choice, app):
    from menuLogic import mainMenu

    difficulties = {
        "1": "easy",  # Changed from random.randint(4, 5)
        "2": "medium",  # Changed from random.randint(6, 7)
        "3": "hard",  # Changed from random.randint(8, 22)
    }

    word_lengths = {
        "easy": random.randint(4, 5),
        "medium": random.randint(6, 7),
        "hard": random.randint(8, 22),
    }
    if choice in difficulties:
        app.app.difficulty = difficulties[choice]  # Store "easy", "medium", "hard"
        if app.mode == "difficultyForHighScores":
            log.info(f"choice = {choice}")
            log.info(f"difficulties[choice] = {difficulties[choice]}")
            app.app.highscores_difficulty = difficulties[choice]
            log.info(f"app.app.highscores_difficulty = {app.app.highscores_difficulty}")
            app.app.push_screen("HighScoresScreen")
        else:
            app.app.word_length = word_lengths[
                app.app.difficulty
            ]  # Store the actual length
            mainGame.initGame(app)
            app.app.push_screen("GameScreen")

    elif choice == "4":
        app.currentScreen = "menu"
        app.mode = "menu"
        app.query_one("#menu").update(mainMenu.buildMenuPanel())
