"""
4. Prompt the user to enter a guess.

    I will use an input function and then assign the result to a variable.


5. Check if the guess that is entered is a valid guess.

    For a guess to be considered valid it must (a) check the word length and
    (b) check that the word the user chosen is a real word (valid) by checking
    if it is in the list of words generated earlier. I will need to use and if/else
    statement (i.e. a selection), with a while loop.
"""
from docswithnotes import dictionary_words

while True:
    user_guess = input("Enter your guess or HELP: ").upper()

    if len(user_guess) == 5 and user_guess in dictionary_words:
        #it goes to score function
        break #valid finish
    else:
        print("Guess is not valid. Please try again with a 5 letter word.")