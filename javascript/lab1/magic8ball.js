// Write a program to simulate the classic "Magic Eight Ball
// 1. Print a welcome screen to the user.
// 2. Use the random module's random.choice() to choose a prediction.
// 3. Prompt the user to ask the 8-ball a question like, "will I win the lottery tomorrow?"
// 4. Display the result of the 8-ball.
// 5. Using a while loop, keep asking the user for a question, if they enter 'done', exit

// DOM selectors:
const displayDiv = document.querySelector('#display')
const submitButton = document.querySelector('#submit')

// Variables:
let DefaultText = 'Result...'
let resultText = ''

const predictions = [
  "It is certain",
  "It is decidedly so",
  "Without a doubt",
  "Yes definitely",
  "You may rely on it",
  "As I see it, yes",
  "Most likely",
  "Outlook good",
  "Yes",
  "Signs point to yes",
  "Reply hazy try again",
  "Ask again later",
  "Better not tell you now",
  "Cannot predict now",
  "Concentrate and ask again",
  "Don't count on it",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful"
]

// Functions:
const updateDisplay = (value) => {
  displayDiv.innerText = value
}

// display 0 at first
updateDisplay(DefaultText) 

// submit button event listener
submitButton.addEventListener('click', (evt) => {
  let randomIndex = Math.floor(Math.random() * predictions.length);
  let reply = predictions[randomIndex];
  evt.preventDefault()
  updateDisplay(reply)
})

// while (true) { 
//   let keep_playing = prompt("You may ask another question or enter DONE: ").trim().toLowerCase()
//   if (keep_playing === 'done') {
//     console.log("Goodbye!")
//     break
//   } else {
//     keep_playing
//     console.log(reply)
//   }
// }
