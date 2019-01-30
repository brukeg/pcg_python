"""
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Make a functional solution that utilizes lists the .split() method.

Make it a repeatable game. Prompt the user for whether they'd like to hear the story, using a while loop, until the answer is 'no'. 
You could then ask them if they'd like to make another story, and so on.
"""


silly_word = input("Enter a silly word: ").capitalize()
last_name = input("What is your last name?: ")
illness = input("Enter the name of an illness: ")
plural_noun = input("Enter a pluar noun: ")
silly_word2 = input("Enter another silly word: ").capitalize()
place = input("Name a place: ")
number = input("Enter a number from 1-100: ")
adjectives = input("Now enter three different adjectives separated by a comma: ")
adjective1,adjective2,adjective3 = adjectives.split(',')
 

print("Dear School Nurse:")
print(
	f"{silly_word} {last_name} will not be attending school today. They have come down with a case of {illness} and has horrible {plural_noun} and a/an {adjective1} fever. We have made an appointment with the {adjective2} Dr. {silly_word2}, who studied for many years in {place} and has {number} degrees in pediatrics. They will send you all the information you need. Thank you!"
	)
print("Sincerely")
print(f"Mrs. {adjective3}.") 