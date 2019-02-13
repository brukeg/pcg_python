"""
 Create a number guessing game. The computer will guess a random int between 1 and 10.
 The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Version 2
Allow the user to make an unlimited number of guesses using a while True and break.
Keep track of how many guesses the user has made, and tell them at the end.

Version 3
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

Version 4 (optional)
Tell the user whether their current guess is closer than their last.
This can be done by maintaining a variable containing the last guess outside the loop,
then comparing the last guess to the current guess, and check if it's closer.
Hint: you're interested in comparing the two absolute differences:
abs(current_guess-target) and abs(last_guess-target).

Version 5 (optional)
Swap the user with the computer: the user will pick a number,
and the computer will make random guesses until they get it right.
 """

import random
number = str(random.randint(1, 10))
guesses = []
print(number)


while True:
    guess = input("Guess a number between 1 and 10: ")
    guesses.append(guess)

    if guesses[-1] == number:
        print(f"Nice, after {len(guesses)}, you guessed the right number!")
        break

    # elif len(guesses) == 10: 
    #   print("Sorry buster you lose!")
    #   break

    elif int(guess) > int(number):
        print("that's too high")
    elif int(guess) < int(number):
        print("That's too low")

    # elif int(guesses[-1])-int(number) < int(guesses[-2]-int(number)):
    #   print("That's closer than your last guess")

    # elif int(guesses[-1])-int(number) > int(guesses[-2]-int(number)):
    #   print("That's farther away than your last guess")

    else:
        print("Hrmm, try again.")
        continue
