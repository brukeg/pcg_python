"""
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

v2:
Allow the user to input the amount of rotation used in the encryption / decryption. eg. rot_n
"""

english_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rot_13 = ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']

def combine(a, b):
	return {a[i]: b[i], for i in range(0, len(a))}

decrypt_dict = combine(english_alphabet, rot_13)

# work with indices