"""
convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Have the user enter a dollar amount (1.36), convert this to the total in pennies.
"""

# get the input, make quarters, subtract quaters from the input, then get dimes from what's left over...

dollar_amount = input("What's the total amount?: ")

total = int(dollar_amount) * 100
quarters = int(total // 25)
dimes = int(total // 10)
nickles = int(total // 5)
pennies = int(total // 1)

print(f"There are {quarters} whole quarters, or {dimes} whole dimes, or {nickles} whole nickles, or {pennies} pennies in {total/100}.")

pennies = input(f"Enter another dollar amount, but this time give me the total number of pennies: ")
dollar_amount = int(pennies) / 100
print(f"That's a dollar amount of ${dollar_amount}.")

dollars = input(f"Now, give me a decimal dollar amount, and I'll give you the number of pennies back: ")
pennies_in = int(float(dollars) * 100)
print(f"That's {pennies_in} pennies, yo!")