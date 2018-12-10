#  Modify the program below to use a while loop to
#  allow as many guesses as necessary.
#
# The program should let the player know whether to
#  guess higher or lower, and should print a message
#  when the guess is correct, A correct guess will
#  terminate the if program.
#
#  As an optional extra, allow the player to quit by entering
#  0 (zero) for their guess.
#  This is a modified "Guess the number" game.


import random


highest = 100
answer = random.randint(1, highest)

guess = 0
print("Please guess a number between 1 and {}:".format(highest))

while guess != answer:
    guess = int(input())

    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
