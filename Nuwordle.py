dictionary_words = []

with open('all_words.txt', 'r') as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                cleaned_word = word.strip()
                dictionary_words.append(cleaned_word)

target_words = []

with open('target_words.txt', 'r') as file:
        for line in file:
            target_word_list = line.split()
            for word in target_word_list:
                target_cleaned_word = word.strip()
                target_words.append(target_cleaned_word)

import random
random_word = random.choice(target_words).upper()
print("random word:", random_word)

def score_guess(guess, target):
    """
    Function scores a guess word against the target word.
    Where
        2: Correct letter, correct position
        1: Correct letter, wrong position
        0: Incorrect letter.
   Args:
       guess (str): The guess word.
       target (str): The target word.
    Returns:
        list: The score of each character in the guess word.
    For example:
        score_guess('world', 'world') returns [2, 2, 2, 2, 2]
    """

    target_list = list(target)
    guess_list = list(guess)
    score = [0, 0, 0, 0, 0]

    for index in range(5):

        if guess_list[index] == target_list[index]:
            score[index] = 2
        elif guess_list[index] in target_list:
            score[index] = 1
        else:
            score[index] = 0
    return score  # return list of scores

def display_instructions():
    """Displays the game instructions to the player."""
    print("WElCOME TO NUWORDLE!")
    print("-" * 30)
    print("Try to guess the secret 5-letter word.")
    print("After each guess, you'll receive a score for each letter:")
    print("  2: Correct letter in the correct position.")
    print("  1: Correct letter but in the wrong position.")
    print("  0: Incorrect letter (not in the target word).")
    print("-" * 30)
    print("You have 6 attempts to guess the word.")
    print("-" * 30)
    print("Example")
    print("Your Guess:   O C E A N")
    print("Score:        1 0 0 0 0")
    print("Target Word:  W O R L D")
    print("-" * 30)
    print("Your Guess:   S T A R E")
    print("Score:        0 1 0 1 1")
    print("Target Word:  T R A C E")
    print("To access these instructions again at any time, type 'HELP'.")
    print("-" * 30)
    print("Good luck!")

show_instructions = input("Would you like instructions? yes/no: ").lower()

if show_instructions == 'yes':
    display_instructions()

count = 0
while count < 6:
    user_input = input("Enter your guess or HELP: ").upper()
    guess_ok = False #while input the word is set to false but if below then true

    for guess in dictionary_words:
        if guess.upper() == user_input:
            guess_ok = True
    #else no needed because only need ==

    #
    if user_input == 'HELP':
       display_instructions()
    elif len(user_input) != 5 or guess_ok == False: #debug:or user_input not in dictionary_words: -> guess_ok
        print("Guess is not valid. Please try again with a 5 letter word from the list.")
    else:
        count = count + 1
        print(user_input + '-' + random_word)
        result = score_guess(user_input,random_word)
        print("Your score is: ", result)
        if result == [2, 2, 2, 2, 2]:
            print("You guessed the NUWORDLE!")
            break
    if count == 6: #can use elif
        print("You Lost")
