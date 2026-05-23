import json
import os
from datetime import date


class HighScoresManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if os.path.exists(self.filepath):
            return
        else:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            structure = {"easy": [], "medium": [], "hard": []}
            with open(self.filepath, "w") as f:
                json.dump(structure, f, indent=2)

    def get_scores(self, difficulty):
        try:
            with open(self.filepath, "r") as f:
                high_scores = json.load(f)
            high_scores[difficulty].sort(key=lambda x: x["score"], reverse=True)
            return high_scores[difficulty]
        except Exception as e:
            print(f"Error reading high scores: {e}")
            return []

    def get_top_n(self, difficulty, n=5):
        scores = self.get_scores(difficulty)
        top_n = scores[:n]
        return top_n

    def is_high_score(self, difficulty, score):
        return True  # I want to save all scores

    def save_score(self, difficulty, firstname, initial_or_lastname, score):
        try:
            date_str = date.today().strftime("%d-%m-%Y")
            with open(self.filepath, "r") as f:
                high_scores = json.load(f)
            new_entry = {
                "firstname": firstname,
                "initial_or_lastname": initial_or_lastname,
                "score": score,
                "date": date_str,
            }
            high_scores[difficulty].append(new_entry)

            high_scores[difficulty].sort(key=lambda x: x["score"], reverse=True)
            with open(self.filepath, "w") as f:
                json.dump(high_scores, f, indent=2)

        except Exception as e:
            print(f"Error saving high score: {e}")
