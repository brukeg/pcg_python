"""
write a python program to give basic blackjack playing advice during a game by asking the player for cards.
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.
At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand.
Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For
one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
"""

# If "A' duplicate values


values = {'a':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'j':10, 'q':10, 'k':10, 'a2':11}

first = input("What's your first card?: ").strip().lower()
second = input("What's your second card?: ").strip().lower()
third = input("What's your second card?: ").strip().lower()

def aces(a, b, c):
	cards = [first, second, third]
	cards2 = []
	have_ace = False
	first_total = values[first] + values[second] + values[third]
	for i in cards:
		if i == 'a' and not have_ace:
			cards2.append(values['a2'])
			have_ace = True
		else:
			cards2.append(values[i])
	second_total = cards2[0] + cards2[1] + cards2[2]

print(advise(first, second, third))
	
def advise(a, b, c):
	if first_total < 17:
		return "Hit"
	elif 17 <= first_total < 21:
		return "Stay"
	elif first_total == 21:
		return "Blackjack!"
	else:
		return "Already Busted"

	
	# if second_total < 17:
	# 	return "Hit"
	# elif 17 <= second_total < 21:
	# 	return "Stay"
	# elif second_total == 21:
	# 	return "Blackjack!"
	# else:
	# 	return "Already Busted"  

print(advise(first, second, third))

