## JSON File Structure
**File location:** `data/highscores.json`

**Format:**
```json
{
  "easy": [
    {"firstname": "Alice", "initial_or_lastname": "Smith", "score": 850, "date": "25-04-2026"},
    {"firstname": "Bob", "initial_or_lastname": "L", "score": 720, "date": "24-04-2026"}
  ],
  "medium": [
    {"firstname": "Charlie", "initial_or_lastname": "O'Brien", "score": 1200, "date": "25-04-2026"}
  ],
  "hard": []
}
```

**Key constraints:**
- All scores ever recorded (no pruning, no cap)
- Sorted by score descending (highest first)
- Date format: DD-MM-YYYY (e.g., "25-04-2026")
- Two separate name fields: `firstname` and `initial_or_lastname` (1-3 characters, varying case)

---

## Auto-Generation on App Start
When app runs (in `main.py` `on_mount`):
```
if data/highscores.json does not exist:
    create data/ folder if needed
    create highscores.json with empty structure:
    {
      "easy": [],
      "medium": [],
      "hard": []
    }
else:
    file already exists, do nothing
```

---

## HighScoresManager Class

**Location:** `gameLogic/highScoresManager.py`

**Imports needed:**
```python
import json
import os
from datetime import date
```

### Method 1: `__init__(self, filepath)`
**Purpose:** Initialise the manager and ensure file exists

**Parameters:**
- `filepath` (str): Path to highscores.json (e.g., "data/highscores.json")

**Logic:**
1. Store `filepath` as `self.filepath`
2. Call `self._ensure_file_exists()`

**Return:** None

---

### Method 2: `_ensure_file_exists(self)`
**Purpose:** Create JSON file if it doesn't exist

**Parameters:** None

**Logic:**
1. Check if file exists: `os.path.exists(self.filepath)`
2. If NO:
   - Create parent directory: `os.makedirs(os.path.dirname(self.filepath), exist_ok=True)`
   - Create default JSON structure (3 empty difficulty arrays)
   - Write to file using `json.dump()`
3. If YES:
   - Do nothing

**Return:** None

---

### Method 3: `get_scores(self, difficulty)`
**Purpose:** Get all scores for a difficulty

**Parameters:**
- `difficulty` (str): "easy", "medium", or "hard"

**Logic:**
1. Try to read and parse JSON file
2. Get the list for that difficulty
3. Return list sorted by score descending (highest first)
4. If difficulty doesn't exist or file is corrupted, return empty list `[]`

**Return:** List of score dicts or empty list

**Example return:**
```python
[
  {"firstname": "Alice", "initial_or_lastname": "Smith", "score": 850, "date": "25-04-2026"},
  {"firstname": "Bob", "initial_or_lastname": "L", "score": 720, "date": "24-04-2026"}
]
```

---

### Method 4: `get_top_n(self, difficulty, n=5)`
**Purpose:** Get top N scores for a difficulty (for display screen)

**Parameters:**
- `difficulty` (str): "easy", "medium", or "hard"
- `n` (int): Number of top scores to return (default 5)

**Logic:**
1. Call `self.get_scores(difficulty)` to get all scores
2. Slice list to first n items: `scores[:n]`
3. Return sliced list

**Return:** List of top N scores or empty list if fewer than N exist

**Example:**
```python
get_top_n("easy", 5)
# Returns top 5 easy scores
```

---

### Method 5: `is_high_score(self, difficulty, score)`
**Purpose:** Check if a score qualifies as a high score

**Parameters:**
- `difficulty` (str): "easy", "medium", or "hard"
- `score` (int): Score to check

**Logic:**
- Always return `True`
- (Reason: You're storing ALL scores, so any score is worth saving)

**Return:** Boolean (always True)

---

### Method 6: `save_score(self, difficulty, firstname, initial_or_lastname, score)`
**Purpose:** Save a new score to the JSON file

**Parameters:**
- `difficulty` (str): "easy", "medium", or "hard"
- `firstname` (str): Player's first name
- `initial_or_lastname` (str): Player's initial or last name (1-3 chars, varying case)
- `score` (int): Score value

**Logic:**
1. Generate today's date: `date.today().strftime("%d-%m-%Y")`
2. Read JSON file
3. Create new entry dict:
   ```python
   new_entry = {
       "firstname": firstname,
       "initial_or_lastname": initial_or_lastname,
       "score": score,
       "date": date_str
   }
   ```
4. Add entry to `data[difficulty]` list
5. Sort difficulty's scores by score descending:
   ```python
   data[difficulty].sort(key=lambda x: x['score'], reverse=True)
   ```
6. Write updated JSON back to file using `json.dump()`

**Return:** None

---

## Error Handling Strategy

**If JSON file is corrupted:**
- `get_scores()` returns empty list `[]`
- `get_top_n()` returns empty list `[]`
- `save_score()` tries to read, fails gracefully, recreates file with new entry

**If difficulty key is missing:**
- `get_scores()` returns empty list `[]`
- `save_score()` creates it

**If name fields are empty:**
- Save as-is (validation happens in UI screen, not here)

---

## Testing Checklist

Before moving to UI screens:
- [x] Create HighScoresManager instance
- [x] Call `_ensure_file_exists()` → file created
- [x] Save 3 scores for "easy" with different values
- [x] Read with `get_scores("easy")` → all 3 returned
- [x] Read with `get_top_n("easy", 2)` → top 2 returned
- [x] Verify scores sorted descending
- [x] Restart app → file persists, scores still there
- [x] Save score to "medium" and "hard" → all difficulties work

---

## Quick Reference

```python
# Import
from gameLogic.highScoresManager import HighScoresManager

# Create instance
hsm = HighScoresManager("data/highscores.json")

# Get all easy scores
all_easy = hsm.get_scores("easy")

# Get top 5 medium scores
top_5_med = hsm.get_top_n("medium", 5)

# Check if score qualifies
qualifies = hsm.is_high_score("hard", 2000)  # Always True

# Save a score
hsm.save_score("easy", "Alice", "Smith", 850)

# Save anonymous score
hsm.save_score("medium", "Anonymous", "?", 1200)
```
