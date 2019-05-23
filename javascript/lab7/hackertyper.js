/* 
Let's create something similar to this and this. 
You can use a textarea or pre to preserve the formatting 
(html will otherwise strip leading and trailing spaces). 
Every time the user presses a key, you can add another 
character to the displayed text. If you use a textarea, 
use event.preventDefault() to stop the original character from being typed.
*/

// DOM Selectors:
const codeArea = document.querySelector('.hacker-area')

// Functions:
function code() {
  fetch('snake.txt')
    .then(response => response.text())
    .then((data) => {
      console.log(typeof(data))
      
    })   
}
const updateDisplay = (value) => {
  codeArea.innerText = value
}

// Function call & Default display text
console.log(code())
updateDisplay('Start typing...')


// Event listeners
codeArea.addEventListener("keydown", (event) => {
  event.preventDefault()

    // console.log(data.length)
    // let list = []
    // for (let i = 0; i < data.length; i++) {
    //   list += data[i]
    // }
    // updateDisplay(data)
    // console.log(list)
})



/*
var rtn= new RegExp("\n", "g"); // newline regex
var rts= new RegExp("\\s", "g"); // whitespace regex
var rtt= new RegExp("\\t", "g"); // tab regex
*/