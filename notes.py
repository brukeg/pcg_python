# 1/31

# https://github.com/DED8IRD/20190128-Python-Fullstack-Night/blob/master/1%20Python/practice/practice01-fundamentals.md
# practice problem 1:
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)


def is_even(a):
	if a % 2 == 0:
		return True
	else:
		return False

# practice problem 2:
# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
	if a >= 0 and b > 0:
		return False
	elif a < 0 an b < 0:
		return False
	else:
		return True

# 1/30

# loop_example.py 
'''while True:
	# input validation
	while True:
		keep_looping = input("Keep looping? ").lower().strip()
		if keep_looping in ['yes', 'no', 'y', 'n']:
			break
		print("Invalid input")
	if keep_looping.startswith('y'):
		continue
	print("Done looping")
	break'''

# defining_functions.py
def greet(name, age, location):
	print(f"Hi! My name is {name}. I am {age} years old, and I come from {location}.")

# optional keyword agrs should go last
def greet_kwarg(name, age, location='anonymous'):
	print(f"Hi! My name is {name}. I am {age} years old, and I come from {location}.")

# *args allows for an optional number of arguments
def sum(*args):
	# a simple sum function
	running_sum = 0
	for num in args:
		running_sum += num

# *kwargs allows for an optional number of keyword arguments
def make_contact(**kwargs):
	defaults = {'name': 'anonymous', 'phone': 'N/A', 'email': 'N/A'}
	print(type(kwargs), kwargs)
	defaults.update(kwargs)
	return defaults

def no_joe(name):
	print('Hello! You are in function no_joe')
	if name.strip().lower().startswith('joe'):
		return "Not allowed in this club. Joe knows why!"
	print('Welcome to Club No Joe')
	print("You're and executive.")

def separate_keys_and_value(dictionary):
	return list(dictionary.keys()), list(dictionary.values())

# args are positional
greet('Larry', 35, "Boca Raton")
greet(age=99, name='ethel', location='FL')

# location is optional
greet_kwarg('Jerry', 26)

# *args takes as many arugments as you like
print(sum(23,2,5,1,44,-13))

# **kwargs also takes as many key word pairs as you like and can have defaults
print(make_contact(age=99, name='ethel', location='FL')

print(no_joe('joeseph'))
print(no_joe('jose'))

# python automatically returns a tuple
print(separate_keys_and_value({'a': 'apples', 'b': 'buffet'}))

# unpacking tuples
keys, values = separate_keys_and_value({'a': 'apples', 'b': 'buffet'})
print(keys, values)

