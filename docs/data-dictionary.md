| Variable Name    | File/Context                             | Type                               | Description / Purpose                              |
| ---------------- | ---------------------------------------- | ---------------------------------- | -------------------------------------------------- |
| word             | main.py (class theLabyrinth, self.word)  | str                                | The current word for the game.                     |
| word_length      | main.py (self.word_length)               | int/None                           | Length of the current word.                        |
| difficulty       | main.py (self.difficulty)                | str/None                           | Current game difficulty.                           |
| remainingGuesses | main.py (self.remainingGuesses)          | int                                | Number of guesses left for the current round.      |
| correctGuesses   | main.py (self.correctGuesses)            | int                                | Number of correct guesses in the round.            |
| incorrectGuesses | main.py (self.incorrectGuesses)          | int                                | Number of incorrect guesses in the round.          |
| guessedLetters   | main.py (self.guessedLetters)            | list                               | List of guessed letters in the round.              |
| stageNumber      | main.py (self.stageNumber)               | int                                | Tracks round/stage (1–3 for Labyrinth game cycle). |
| totalScore       | main.py (self.totalScore)                | int                                | Cumulative score across rounds.                    |
| stageScore       | main.py (self.stageScore)                | list                               | Stores score for each round.                       |
| DEBUG            | main.py                                  | bool                               | Developer debug flag/toggle.                       |
| menu             | menuLogic/mainMenu.py (buildMenuPanel)   | Panel                              | The actual rendered Rich menu panel.               |
| t                | menuLogic/mainMenu.py (buildMenuPanel)   | Text                               | The title/text of the menu.                        |
| selections       | menuLogic/mainMenu.py (buildMenuPanel)   | Text                               | The options for the menu.                          |
| console          | styles/displayPixelArt.py                | Console                            | Rich Console object for rendering output.          |
| pixels           | styles/displayPixelArt.py                | Pixels/Align/Panel                 | Pixel art or boxed Pixel art for logo display.     |
| con, cur         | gameLogic/dbUtils.py (wordDB)            | sqlite3.Connection/ sqlite3.Cursor | Database connection/manager for SQLite.            |
| row              | gameLogic/dbUtils.py                     | tuple                              | Row result from database queries.                  |
| definition       | gameLogic/dbUtils.py (getWordDefinition) | str                                | Definition string from the database.               |
| pos              | gameLogic/dbUtils.py (getWordDefinition) | str                                | Part of speech from the DB.                        |
| e                | gameLogic/dbUtils.py (exception)         | Exception                          | Exception for DB error handling.                   |
