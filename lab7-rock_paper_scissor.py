"""
Let's play rock-paper-scissors with the computer.

1. The computer will ask the user for their choice (rock, paper, scissors)
2. The computer will randomly choose rock, paper or scissors
3. Determine who won and tell the user

4. optional: 
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.
"""
import random

def calc_winner(comp_choice, user_choice):
	defeats = {
		'rock': 'scissor', 
		'paper': 'rock', 
		'scissor': 'paper'
	}

	if comp_choice == user_choice:
		return 'Tie'
	elif defeats[user_choice] == comp_choice:
		return "User wins!"
	else:
		return "Computer wins!"

valid_choice = ['rock', 'paper', 'scissor']
while True:
	user_choice = input("What'll it be rock, paper, or scissor? ").strip().lower()
	if user_choice not in rps:
		break
	print("You can only choose between rock, paper, or scissor")
computer_choice = random.choice(valid_choice)
print(computer_choice)

print(calc_winner(computer_choice, user_choice)