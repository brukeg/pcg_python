"""
A palindrome is a word that's the same forwards or backwards. Two words are anagrams of eachother if the 
letters of one can be rearranged to fit the other. Write a palindrome and anagram checker. 

"""

def check_palindrome(word):
	reverse = ''
	word = input("Enter a word: ").strip().lower()
	for l in word:
		reverse = l + reverse
	if reverse == word:
		return f"{word} is a palindrome!"
	else:
		return f"{word} is not a palindrome."

def check_anagram(word1, word2):
	# strip and lower the inputs
	word1 = input("Enter the first word: ").strip().lower()
	word2 = input("Enter the second word: ").strip().lower()

	# replace white space between words and sort
	result1 = sorted(word1.replace(" ", ""))
	result2 = sorted(word2.replace(" ", ""))
	
	if result1 == result2:
		return f"{word1} and {word2} are anagrams!"
	else:
		return f"{word1} and {word2} are not anagrams."