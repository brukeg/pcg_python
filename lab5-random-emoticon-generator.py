"""
Generate emoticons by randomly choosing a set of eyes, a nose, and a mouth. 
Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon

Use a loop to generate 5 emoticons.
"""

import random

eyes = [":", ";", "="]
noses = ["-", "^", ""]
# backslash is escape so you have to type it twice to use it in a string.
mouths = ["D", "P", "\\"] 

iterations = 0
while iterations < 5:
	eye_choice = random.choice(eyes)
	nose_choice = random.choice(noses)
	mouth_choice = random.choice(mouths)
	
	assembly = eye_choice + nose_choice + mouth_choice
	print(assembly)
	iterations += 1