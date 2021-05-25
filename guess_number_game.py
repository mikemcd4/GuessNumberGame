# Guess the number game

import random

# Get players name + greet player
print('Hello, what is your name?')
name = input()

print('Howdy there, ' + name + ', I am thinking of a number between 1 and 100.')

# Assign random number between 1 & 100 to secretNumber variable
secretNumber = random.randint(1, 100)

# Create for loop for player to guess a number in 10 tries and print hints
for guessesTaken in range(1, 11):
    print('Take a guess.')
    player_guess = int(input())

    if player_guess < secretNumber:
        print('Your guess was too low.')

    elif player_guess > secretNumber:
        print('Your guess was too high.')
    else:
        break # This condition is for the correct guess

# Win / Lose Situation
if player_guess == secretNumber:
    print('Great job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry! The number I was thinking of was ' + str(secretNumber))


