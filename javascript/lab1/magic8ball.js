// Write a program to simulate the classic "Magic Eight Ball
// 1. Print a welcome screen to the user.
// 2. Use the random module's random.choice() to choose a prediction.
// 3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
// 4. Display the result of the 8-ball.
// 5. Using a while loop, keep asking the user for a question, if they enter 'done', exit


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

console.log("Welcome to the fucking MAGIC 8-ball of glory!!");
prompt("Ask your question wisely: ").trim().toLowerCase();
let reply = Math.random(predictions);
console.log(reply);

while (true) { 
  let keep_playing = prompt("You may ask another question or enter DONE: ").trim().toLowerCase()
  if (keep_playing === 'done') {
    console.log("Goodbye!")
    break
  } else {
    keep_playing
    console.log(reply)
  }
}