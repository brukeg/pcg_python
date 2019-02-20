"""
Write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

- Convert the input string into a list of ints
- Slice off the last digit. That is the check digit.
- Reverse the digits.
- Double every other element in the reversed list.
- Subtract nine from numbers over nine.
- Sum all values.
- Take the second digit of that sum.
- If that matches the check digit, the whole card number is valid.
"""

credit_card = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
def ccv(number_string):
	string_to_list = number_string.split(' ')
	check_digit = string_to_list[-1]
	slice_off = ''.join(string_to_list.pop())
	reverse = string_to_list[::-1]
	reverse[::2] = [int(n)*2 for n in reverse[::2]]
	minus_nine = []
	addition = 0
	
	for i in reverse:
		if int(i) > 9:
			minus_nine.append(int(i) - 9)
		else:
			minus_nine.append(int(i))
	
	for i in minus_nine:
		addition += i
	first_index = str(addition)[1]
	
	if first_index == check_digit:
		return "Valid!"
	else:
		return "Not valid"

print(ccv(credit_card))

