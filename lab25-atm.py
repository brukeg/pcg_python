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
        self.transactions = []

    def check_balance(self):
        return f"Your balance is ${self.balance}."

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit of ${amount}")
        print(f'Your deposit of ${amount} was successful and your current balance is ${self.balance}')

    def check_withdraw(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        if self.check_withdraw(amount):
            self.balance -= amount
            self.transactions.append(f'Withdraw of ${amount}.')
            print(f'Your withdraw of ${amount} was successful and your current balance is ${self.balance}')
        else:
            print('Insufficient funds for this transaction')

    def print_transactions(self):
        for counter, transaction in enumerate(self.transactions):
            print(counter+1, transaction)


def main():
    atm = Atm()
    loop = True
    valid_inputs = [
        'd', 'deposit',
        'w', 'withdraw',
        'c', 'check balance',
        'h', 'history',
        'o', 'commands',
        'e', 'exit'
        'help', 'quit'
    ]
    commands = """
        Commands:
        (d)eposit
        (w)withdraw
        (c)heck balance
        (h)istory
        c(o)mmands
        (e)xit
    """

    print("Welcome to the ATM.")
    print(commands)

    while loop:
        print('-'*80)
        valid = False

        while not valid:
            print("What would you like to do?")
            cmd = input('cmd> ').strip().lower()
            if cmd in valid_inputs:
                valid = True
            else:
                print('Invalid input!')
                print(commands)

        if cmd in ['d', 'deposit']:
            amount = int(input('How much would you like to deposit? '))
            atm.deposit(amount)

        elif cmd in ['w', 'withdraw']:
            amount = int(input('How much would you like to withdraw? '))
            atm.withdraw(amount)

        elif cmd in ['c', 'check balance']:
            print(atm.check_balance())

        elif cmd in ['h', 'history']:
            print("Transaction history:")
            if len(atm.transactions) > 0:
                atm.print_transactions()
            else:
                print("0 transactions")

        elif cmd in ['o', 'commands', 'help']:
            print(commands)

        elif cmd in ['e', 'exit', 'quit']:
            loop = False
            print('Thank you, goodbye!')


if __name__ == '__main__':
    main()
    