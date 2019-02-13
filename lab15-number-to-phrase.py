"""
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
Hint: you can use modulus to extract the ones and tens digit.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.

"""
print(10 % 100)
print(11 % 100)
print(67 % 10)
print(10 // 10)
print(11 // 10)
print(67 // 10)

ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens ={0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen',8: 'eighteen', 9: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'sevnty', 8: 'eight', 9: 'ninety'}


def number_to_phrase(integer):
    """
    return a english word representation of a integer between 0-99
    """
    if integer > 19 and ones_digit != 'zero':
            tens_digit = ''
            for key in tens:
                if integer // 10 == key:
                    tens_digit += tens[integer // 10]
        
        if integer // 10 == 1:
            teenth = ''
            for key in teens:
                if integer % 10 == key:
                    teenth += teens[integer % 10]
            
            if integer < 10 or integer > 19:
                ones_digit = ''
                for key in ones:
                    if integer % 10 == key:
                        ones_digit += ones[integer % 10]

            return tens_digit + '-' + ones_digit


print(number_to_phrase(21))