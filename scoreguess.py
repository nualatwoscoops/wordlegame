#Nuala Malone 2014555 01/04/2025

#guess = input("What is your guess?")
#target = "OCEAN"

guess = 'world'
print("Guess:", guess)
target = 'world'
print("Target:", target)

def score_guess(guess, target):
    score = [0, 0, 0, 0, 0]
    if guess == target:
        score = [2, 2, 2, 2, 2]
    return score

result = score_guess(guess, target)
print("Got:", score_guess(guess, target))
print("Expected:", [2, 2, 2, 2, 2])