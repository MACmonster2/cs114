"""This is a guess the number game."""

import random
from time import sleep
secret_number = random.randint(1, 30)

print('I am thinking of a number between 1 and 30.')
sleep (1)
#Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Too low, try again.')
    elif guess > secret_number:
        print('Too high, try again.')
    else:
        break    #This condition is the correct guess!

if guesses_taken == 1:
    print('Amazing! Getting it on the first try is difficult!')
if guess == secret_number:
    print('Great job! You got my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Your guess was incorrect. The number I was thinking of was ' + str(secret_number))
