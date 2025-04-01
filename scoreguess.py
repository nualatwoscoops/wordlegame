#Nuala Malone 2014555 01/04/2025

guess = input("What is your guess?")
target = "OCEAN"

def score_guess(guess, target):
    score = [0, 0, 0, 0, 0]
    if guess == target:
        score = [2, 2, 2, 2, 2]
        return score
print(score_guess(guess, target))