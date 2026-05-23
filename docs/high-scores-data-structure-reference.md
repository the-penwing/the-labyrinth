## Top Level: Dictionary
```python
{
  "easy": [...],
  "medium": [...],
  "hard": [...]
}
```

Three keys (difficulties), each containing a list.

---

## Each Difficulty: List of Dictionaries

```python
"easy": [
  {"firstname": "Alice", "initial_or_lastname": "S", "score": 850, "date": "25-04-2026"},
  {"firstname": "Bob", "initial_or_lastname": "J", "score": 720, "date": "24-04-2026"},
  {"firstname": "Charlie", "initial_or_lastname": "C", "score": 600, "date": "23-04-2026"}
]
```

Each difficulty contains a **list** of score entries.
**Scores sorted highest first** (850 → 720 → 600).

---

## Each Score Entry: Dictionary

```python
{
  "firstname": "Alice",           # string - player's full name
  "initial_or_lastname": "S",     # string - 1-3 characters
  "score": 850,                   # integer - the score value
  "date": "25-04-2026"            # string - DD-MM-YYYY format
}
```

Four fields per score entry.

---

## Full Example

```python
{
  "easy": [
    {"firstname": "Alice", "initial_or_lastname": "S", "score": 850, "date": "25-04-2026"},
    {"firstname": "Bob", "initial_or_lastname": "J", "score": 720, "date": "24-04-2026"}
  ],
  "medium": [
    {"firstname": "Charlie", "initial_or_lastname": "W", "score": 1200, "date": "25-04-2026"},
    {"firstname": "Diana", "initial_or_lastname": "P", "score": 980, "date": "24-04-2026"}
  ],
  "hard": []
}
```

---

## Python Type Annotation (If You Care)

```python
Dict[str, List[Dict[str, Union[str, int]]]]
```

In plain English:
- **Dict** with string keys ("easy", "medium", "hard")
- Each value is a **List** of dictionaries
- Each dictionary has string keys and values that are either **strings or integers**

---

- Scores **must be sorted highest first** per difficulty
- Date format is always **DD-MM-YYYY** (e.g., "25-04-2026")
- Two name fields: full name + initial/lastname (1-3 chars)
- All three difficulty keys must exist (even if empty)