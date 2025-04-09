""""1. Present game instructions to player (That is, display an output to the screen).

    The senior developer emphasized that the game must include instructions that
    appear the first time the user plays the game and can be accessed any time by
    entering “HELP” in any case. The developer said I should use a print
    function for each line.
"""

"""WElCOME TO NUWORDLE
Scream at computer in your chosen language to continue
Excellent. You have chosen English. Let's Play.

A random 5 letter word has been chosen for you.
Your mission is to guess this 5 letter word within 6 tries.
But fear not, you will be armed with an amazing scoring system.

After entering your guess word the scores will appear as:
2: you correctly guessed a letter and it is in the right position
1: you correctly guessed a letter and it is in the wrong position
0: no, this letter is not in the word at all.

E.G.
Your Guess:   O C E A N
Score:        1 0 0 0 0
Target Word:  W O R L D

Your Guess:   S T A R E
Score:        0 1 0 1 1
Target Word:  T R A C E

Type Help for help.

You have 6 tries. Good luck!

"""

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

show_instructions = input("Would you link instructions? yes/no: ").lower()

if show_instructions == 'yes':
    display_instructions()

while True:
    user_input = input("Enter your guess or HELP: ").upper()
    if user_input == 'HELP':
       display_instructions()



