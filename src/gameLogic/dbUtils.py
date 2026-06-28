# import DB managment libary
import sqlite3


class wordDB:
    # defining attributes
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()

    # picking the random word from the database
    def getRandomWord(self, length):
        self.cur.execute(
            """
            SELECT word FROM words
            WHERE length = ?
            ORDER BY RANDOM()
            LIMIT 1
        """,
            (length,),
        )
        row = self.cur.fetchone()
        return row[0] if row else None

    def wordExists(self, word):
        self.cur.execute("SELECT 1 FROM words WHERE word = ?", (word.lower(),))
        return self.cur.fetchone() is not None

    def close(self):
        self.con.close()

    @staticmethod
    def getWordDefinition(word):
        """
        Fetch the definition and part of speech from the local database.
        Returns formatted string like: "A greeting (noun)"
        """
        con = None
        try:
            con = sqlite3.connect("data/words.db")
            cur = con.cursor()

            cur.execute(
                "SELECT definition, part_of_speech FROM words WHERE word = ?",
                (word.lower(),),
            )
            row = cur.fetchone()

            if row:
                definition, pos = row
                if pos and pos != "":
                    return f"{definition} ({pos})"
                return definition

            return "Definition not available"
        except Exception as e:
            return "Definition not available"
        finally:
            if con:
                con.close()


"""
Database utilities for word management.
Uses SQLite to store words, lengths, definitions, and parts of speech.
Definitions are fetched from dictionaryapi.dev during build time and stored locally.
"""
