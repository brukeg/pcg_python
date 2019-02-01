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

valid_choices = ['rock', 'paper', 'scissor']
play_game = True
rps_valid = True

# valid_inputs = ['yes', 'no', 'y', 'n']
while play_game:
	play = input('Do you want to play rps, yes/no?: ').lower().strip()
	if play == 'yes' or play == 'y':
		# while loop for RPS validiation 
		while rps_valid:
			your_choice = input("What'll it be rock, paper, or scissor? ").strip().lower()
			print("Your choice: " + your_choice)
			if your_choice in valid_choices:
				computer_choice = random.choice(valid_choices)
				print("I chose: " + computer_choice)
				print(calc_winner(computer_choice, your_choice))
				rps_valid = False
			else:
				print("You can only choose between rock, paper, or scissor")
	elif play == 'no' or play == 'n':
		#if play.startswith('n'):
		print("Goodbye!")
		play_game = False
	else: 
		# print("Not Valid Response")	
		print("Enter yes, no, y, or n only!")

	