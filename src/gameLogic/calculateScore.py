def totalPoints(correctGuesses, incorrectGuesses):
    points = 50
    for i in range(correctGuesses):
        points = points + 15
    for i in range(incorrectGuesses):
        points = points - 5
    return points


def findScore(remainingGuesses, points):
    score = int(points) * int(remainingGuesses)
    return score


"""
- Players start at 50 points they then gain 15 points for every correct guess and lose 5 for each incorrect guess the total score at the end is multiplied by the number of remaining guesses
- Players Start with 15 guesses
"""
