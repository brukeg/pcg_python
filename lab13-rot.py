"""
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

v2:
Allow the user to input the amount of rotation used in the encryption / decryption. eg. rot_n
"""

english_alphabet = ['abcdefghijklmnopqrstuvwxyz']
rot_13 = ['nopqrstuvwxyzabcdefghijklm']

def encode(message):
	encoded = ''
	for char in message:
		index = english_alphabet.find(char)
		if index == -1:
			encoded += char
		else:
			encoded += rot13[index]
	return encoded

# work with indices decrypt_dict = combine(english_alphabet, rot_13)
def decode(message):
	decoded = ''
	for char in message:
		index = rot13.find(char)
		if index == -1:
			decoded += char
		else:
			decoded += english_alphabet[index]
	return decoded

def encoded(message, n):
	n %= 26 # wrap around 26
	translate = alphabet[n:] + alphabet[:n]
	encoded = ''
	for char in message:
		index = alphabet.find(char)
		if index == -1:
			encoded += char
		else:
			encoded += translate[index]
	return encoded

def decoded(message, n):
	n %= 26 # wrap around 26
	transalate = alphabet[n:] + alphabet[:n]
	decoded = ''
	for char in message:
		index = transalate.find(char)
		if index == -1:
			encoded += char
		else:
			encoded += alphabet[index]
	return encoded

def cypher(message, n, decode=False):
	n %= 26 # wrap around 26
	transalate = alphabet[n:] + alphabet[:n]
	if decode:
		#decode logic
		codec = translate
		translate = alphabet
	else:
		#encode logic
		codec = alphabet
	coded = ''
	for char in message:
		index = codec.find(char)
		if index == -1:
			coded += char
		else:
			coded += translate[index]
	return coded

def main():
	replay = True
	print('-'*60)
	print('Welcome to the ROT cypher')
	print('-'*60)
	while replay:
		while True:
			operation = input('Do you want to encode or decode?: ').strip().lower()
			if operation in ['encode', 'e', 'decode', 'd']:
				break
		while True:
			try:
				n = int(input("How much do you want to rotate by?: "))
				break
			except ValueError:
				print('Error: enter a whole number.')

		message = input('Enter message to cypher: ')
		if operation.startswith('e'):
			print('-'*60)
			print('Here is your encoded message: ')
			print(cypher(message, n))
			print('-'*60)
		else:
			print('-'*60)
			print('Here is your dencoded message: ')
			print(cypher(message, n, True))
			print('-'*60)

		while True:
			play_again = input("Do yo want to play again?: ").strip().lower()
			if play_again in ['yes', 'y', 'no', 'n']:
				break

			if play_again.startswith('n'):
				replay	= False
				print('-'*60)
				print('Goodbye!')
				print('-'*60)

if __name__ == '__main__':
main()