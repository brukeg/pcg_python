"""
convert a number grade to a letter grade, using if and elif statements and comparisons.

1. Have the user enter a number representing the grade (0-100)
2. Convert the number grade to a letter grade

Optional: 
Find the specific letter grade (A+, B-, etc)
"""

while True:
	user_grade = int(input("Enter your grade as an integer percent > 0: "))
	ones_digit = user_grade % 10

	if user_grade >= 90:
		letter_grade = 'A'
	elif user_grade >= 80:
		letter_grade = 'B'
	elif user_grade >= 70:
		letter_grade = 'C'
	elif user_grade >= 60:
		letter_grade = 'D'
	else:
		letter_grade = 'F'

	# special treatment for handling F grades without a sign
	sign = ''
	if letter_grade != 'F':
		if ones_digit < 4:
			sign = '-'
		elif ones_digit > 7 or letter_grade == 100:
			sign = '+'

	# special treatment for handling 100%
	if letter_grade == 'A':
		if user_grade >= 100:
			sign = '+'
		elif 4 < ones_digit < 100:
			sign = ''

	print(str(letter_grade + sign))

	# read, evaluate, print treatment
	valid_inputs = ['yes', 'no', 'y', 'n']
	while True:
		play_again = input('Do you want to continue: ').lower().strip()
		if play_again in valid_inputs:
			break
		else:
			print("Not a valid input")
	if play_again.startswith('n'):
		print("Goodbye!")
		break
