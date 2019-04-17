/*
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
*/

class Atm {
  constructor() {
    this.balance = 0
    this.transactions = []
  }

  checkBalance() {
    let balance = (`Your current balance is \$${this.balance}`)
    return balance
  }

  deposit(amount) {
    this.balance += amount
    this.transactions.push(`Deposit of \$${amount}`)
    let deposit_tx = (`Your deposit of \$${amount} was successful, and your current balance is \$${this.balance}`)
    return deposit_tx
  }

  checkWithdraw(amount) {
    return amount <= this.balance;
  }

  withdraw(amount) {
    if (this.checkWithdraw(amount)) {
      this.balance -= amount
      this.transactions.push(`Withdrawal of \$${amount}`)
      let withdraw_tx = (`Your withdraw of \$${amount} was successful and your current balance is \$${this.balance}`)
      return withdraw_tx
    } else {
      let inf = (`Insufficient funds for this transaction`)
      return inf
    }

  }
 
  showTransactions() {
    let transactions = ''
    for (let [counter, transaction] of this.transactions.entries()) {
      transactions +=  (counter+1) + ' ' + transaction + ', '
    }
    return transactions
  }
}

// DOM Selectors:
const displayDiv = document.querySelector('#display')
const balanceDiv = document.querySelector('#balance')
const depositDiv = document.querySelector('#deposit')
const withdrawDiv = document.querySelector('#withdraw')
const txnDiv = document.querySelector('#transactions')
const digits = document.querySelectorAll('.num')
const decDiv = document.querySelector('#dec')
const ceDiv = document.querySelector('#CE')
const enterDiv = document.querySelector('#enter')

// Variables:
let balance = 0
let itemAmount = ''
let decimal = false

// Functions:
const updateDisplay = (value) => {
  displayDiv.innerText = value
}

const addDigit = (digit) => {
  itemAmount += digit
  updateDisplay(itemAmount)  
}

const addDecimal = () => {
  if (!decimal) {
    itemAmount += '.'
    updateDisplay(itemAmount)
    decimal = true  
  }  
}

const clearEntry = () => {
  itemAmount = ''
  decimal = false
  updateDisplay(balance)  
}

// Starting balance is 0
updateDisplay(balance)

// Instantiate Atm:
const myAtm = new Atm()

// Event Listeners:
digits.forEach(elem => {
  let digit = elem.innerText
  elem.addEventListener('click', () => {
    addDigit(digit)
  })
})

decDiv.addEventListener('click', () => {
  addDecimal()
})

ceDiv.addEventListener('click', () => {
  clearEntry()
})

balanceDiv.addEventListener('click', () => {
  updateDisplay(myAtm.checkBalance())
})

depositDiv.addEventListener('click', () => {
  let amount = parseFloat(itemAmount)
  updateDisplay(myAtm.deposit(amount))
})

withdrawDiv.addEventListener('click', () => {
  let amount = parseFloat(itemAmount)
  updateDisplay(myAtm.withdraw(amount))
})

txnDiv.addEventListener('click', () => {
  updateDisplay(myAtm.showTransactions())
})

enterDiv.addEventListener('click', () => {
  
})

