"""
Generate a password of length n using a while loop and random.choice, this will be a string of random characters.
random.choice can be used to pick a character out of a string, as well as an element out of a list.

Allow the user to enter the value of n, remember to convert its type, as input returns a string.

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters 
they'd like in their password. Generate a password accordingly.
"""

import random

characters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
special = '`~!@#$%^&*()_+=[{]\\}|:;<>?.'

n_lower = int(input("How many lowercase letters do you want?: "))
n_upper = int(input("How many uppercase letters do you want?: "))
n_numbers = int(input("How many numbers do you want?: "))
n_special = int(input("How many special characters do you want?: "))

password = ''

while n_lower > 0:
	lower = random.choice(characters)
	password += lower
	n_lower -= 1

while n_upper > 0:
	upper = random.choice(characters.upper())
	password += upper
	n_upper -= 1

while n_numbers > 0:
	p_numbers = random.choice(numbers)
	password += p_numbers
	n_numbers -= 1

while n_special > 0:
	p_special = random.choice(special)
	password += p_special
	n_special -= 1

# cast password to a list and shuffle it so the output isn't given in the order of the loop.
password = list(password)
random.shuffle(password) 
print("This is your password: " + ''.join(password))
