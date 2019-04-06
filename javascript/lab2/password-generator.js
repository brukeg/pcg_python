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

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array
}

const characters = 'abcdefghijklmnopqrstuvwxyz'
const numbers = '1234567890'
const special = '`~!@#$%^&*()_+=[{]\\}|:;<>?.'

let n_lower = Number(prompt("How many lowercase letters do you want?: "))
let n_upper = Number(prompt("How many uppercase letters do you want?: "))
let n_numbers = Number(prompt("How many numbers do you want?: "))
let n_special = Number(prompt("How many special characters do you want?: "))

let password = ''

while (n_lower > 0) {
  let lower = Math.random(characters)
  password += lower
  n_lower -= 1
}  
  
while (n_upper > 0) {
  let upper = Math.random(characters.toUpperCase())
  password += upper
  n_upper -= 1
}
  
while (n_numbers > 0) {
  let p_numbers = Math.random(numbers)
  password += p_numbers
  n_numbers -= 1
}

while (n_special > 0) {
  let p_special = random.choice(special)
  password += p_special
  n_special -= 1  
}


//cast password to a list and shuffle it so the output isn't given in the order of the loop.
password = password.split('')
shuffleArray(password) 
console.log("This is your password: " + password.join(''))
