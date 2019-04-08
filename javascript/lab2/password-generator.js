// lab2(lab6-password-generator).js

/*
Generate a password of length n using a while loop and random.choice, 
this will be a string of random characters. random.choice can be used 
to pick a character out of a string, as well as an element out of a list.
Allow the user to enter the value of n, remember to convert its type, 
as input returns a string. Ask the user for how many lowercase letters, 
uppercase letters, numbers, and special characters they'd like in their password. 
Generate a password accordingly.
*/

// DOM Selectors:
const lowercaseDiv = document.querySelector('#lowercase')
const uppercaseDiv = document.querySelector('#uppercase')
const numbersDiv = document.querySelector('#numbers')
const specialDiv = document.querySelector('#special')
const submitButton = document.querySelector('#submit')
const displayDiv = document.querySelector('#display')

// Variables:
const characters = 'abcdefghijklmnopqrstuvwxyz'
const numbers = '1234567890'
const special = '`~!@#$%^&*()_+=[{]\\}|:;<>?.'

// Functions:
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array
}

const updateDisplay = (value) => {
  displayDiv.innerText = value
}

const randomItem = (list) => {
  let randomIndex = Math.floor(Math.random() * list.length);
  return list[randomIndex];
}

// Default display text
updateDisplay('...Password') 

// Event listeners
lowercaseDiv.addEventListener('submit', () => {
  const n_lower = document.getElementById("lowercase").value;
})

uppercaseDiv.addEventListener('submit', () => {
  const n_upper = document.getElementById("uppercase").value;
})

numbersDiv.addEventListener('submit', () => {
  const n_numbers = document.getElementById("numbers").value;
})

numbersDiv.addEventListener('submit', () => {
  const n_special = document.getElementById("special").value;
})

submitButton.addEventListener('click', (evt) => {
  let password = ''

  while (n_lower > 0) {
    let lower = randomItem(characters)
    password += lower
    n_lower -= 1
  }  
    
  while (n_upper > 0) {
    let upper = randomItem(characters.toUpperCase())
    password += upper
    n_upper -= 1
  }
    
  while (n_numbers > 0) {
    let p_numbers = randomItem(numbers)
    password += p_numbers
    n_numbers -= 1
  }
  
  while (n_special > 0) {
    let p_special = randomItem(special)
    password += p_special
    n_special -= 1  
  }
  
// Cast password to a list and shuffle it, 
// so the output isn't given in the order of the loop.
  password = password.split('') 
  shuffleArray(password) 
  evt.preventDefault()
  updateDisplay(password.join(''))
})
