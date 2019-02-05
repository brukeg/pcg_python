"""
convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Have the user enter a dollar amount (1.36), convert this to the total in pennies.
"""

# split the input amount by the decimal point since input() returns a string.
amount_list = input("What's the total amount?: ").split('.')

# add the strings together which is the same as times 100, then cast as a integer.
total = int(amount_list[0] + amount_list[1])

quarters = total // 25
sub_total = total-(quarters*25)

dimes = sub_total // 10
sub_total = sub_total-(dimes*10)

nickles = sub_total // 5
sub_total = sub_total-(nickles*5)

pennies = sub_total
	
print(f"There are {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies in ${total/100}.")

pennies = input(f"Enter another dollar amount, but this time give me the total number of pennies: ")
dollar_amount = int(pennies) / 100
print(f"That's ${dollar_amount}.")

dollars = input(f"Now, give me a decimal dollar amount, and I'll give you the number of pennies back: ")
pennies_in = int(float(dollars) * 100)
print(f"That's {pennies_in} pennies, yo!")