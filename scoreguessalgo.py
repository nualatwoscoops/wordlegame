#Start:
    #Get target word
    #Get guess word
    #Set score to list of 0s with len equal to len of target

    #For each index starting from 0, Increment index by 1 after each loop until 5
        #Assess each character in guess
            #If current guess index character = current index target character
                #set score at current index to 2
            #else if current guess index character in target
                # set score at current index to 1
            #else set to score 0

    #If score list is not 22222, loop  to guess word for next try
    #If score list is 22222:
# end game win
#duplicate scores not handled

"""with open('all_words.txt', 'r') as f:
    for line in f:
        words = f.split("")
        if (line.strip()): #function removes unwanted lines
            line =

    all_words = f.readall_words()

lines = [line.replace('\n', '') for line in lines]

with open('all_words.txt', 'r') as f:
    lines = f.read().splitlines()"""


guess = 'ocean'
print("Guess:", guess)
target = 'world'
print("Target:", target)

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
    return score #return list of scores

result = score_guess(guess, target)
print("Result:", result)
print("Expected:", [2, 2, 2, 2, 2])

if result == [2, 2, 2, 2, 2]:
    print("Test passed")
else:
    print("Test failed")

#Note: This code does not handle duplicate characters in the word



