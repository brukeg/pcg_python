"""
Write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication,
and division. Ask the user for an operator and each operand. Don't forget that input returns a string, 
which you can convert to a float using float(user_input) where user_input is the string you got from input. 
Below is some sample input/output.

Version 2
Allow the user to keep performing operations until they say 'done'. Use while True and break. 
Below is some sample input/output.

Version 3 (optional)
Allow the user to enter a full arithmetic expression and use eval to evaluate it.
"""

while True:
	opperand = input("What is the operation you'd like to perform? (or say 'done'): ")
	if opperand == 'done':
		print("Goodbye!")
		break
	elif opperand not in ['+', '-', '*', '/']:
		print("Not valid opperand!")
		break
	else:
		first_num = float(input("What is the first number?: "))
		second_num = float(input("What is the second number?: "))
		def calc(first_num, second_num, opperand):
			if opperand == '+':
				return first_num + second_num
			elif opperand == '-':
				return first_num - second_num
			elif opperand == '*':
				return first_num * second_num
			else:
				return first_num / second_num

	print(calc(first_num, second_num, opperand))
