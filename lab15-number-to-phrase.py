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
unos = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'sevnty', 'eight', 'ninety']
hundo = 'hundred'


def number_to_phrase(integer):
    """
    return a english word representation of a integer between 0-99
    """
    if integer > 99:
        """
        Handle numbers over 99
        """
        num = ''
        if integer % 100 == 0:
            num += str(unos[integer // 100]) + '-' + hundo # hundreds
        if integer % 100 < 10 and integer % 100 != 0:
            num += str(unos[integer // 100]) + '-' + hundo + '-' + unos[integer % 100] # hundred-ones
        if (integer % 100) // 10 == 1:
            num += str(unos[integer // 100]) + '-' + hundo + '-' + teens[(integer % 100) % 10] # hundred-ten/teens
        if integer % 100 > 19:
            if (integer % 100) % 10  == 0:
                num += str(unos[integer // 100]) + '-' + hundo + '-' + tens[(((integer % 100) // 10) - 2)] # hundred-tens
            else:
                num += str(unos[integer // 100]) + '-' + hundo + '-' + tens[(((integer % 100) // 10) - 2)] + '-' + unos[((integer % 100) % 10)] # one-hundred-tens-ones
        return num

    if integer > 19:
        """ 
        Handle any number over 19
        """
        num = ''
        if integer % 10 == 0:
            num += tens[(integer // 10) - 2]
        else:
            num = str(tens[(integer // 10) - 2]) + '-' + (str(unos[integer % 10]))
        return num
        
    if integer // 10 == 1:
        """
        Handle the teens explicitly
        """
        return teens[integer % 10]

    if integer < 10:
        """
        Handle single number digits
        """
        return unos[integer]

print(number_to_phrase(921))
