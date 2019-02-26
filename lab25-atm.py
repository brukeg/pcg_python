"""
represent an ATM with a class containing a balance property. A newly created
account will default to a balance of 0. Implement the initializer, as well as
the following methods:

- check_balance() returns the account balance
- deposit(amount) deposits the given amount in the account
- check_withdrawal(amount) returns true if the withdrawn amount won't put
the account in the negative
- withdraw(amount) withdraws the amount from the account and returns it

Version 2
Have the ATM maintain a list of transactions. Every time the user makes a
deposit or withdrawal, add a string to a list saying 'user deposited $15' or
'user withdrew $15'. Add a new function print_transactions() to your class for
printing out the list of transactions.

Version 3
Allow the user to enter commands into a REPL.

> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5
"""

class Atm():
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return f"Your balance is ${self.balance}."

    def deposit(self, amount):
        self.balance += amount
        return f"Your balance is now ${self.balance}."

    def check_withdraw(self, amount):
        if self.balance - amount < 0:
            return f"Sorry, {amount} is greater than your available balance of {self.balance}" 
        else:
            self.balance -= amount
            return f"Your balance after withdrawal is {self.balance}."

my_atm = Atm()
print(my_atm.check_balance())
print(my_atm.deposit(1000))
print(my_atm.check_withdraw(125))