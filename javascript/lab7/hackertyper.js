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
const updateDisplay = (value) => {
  codeArea.innerText = value
}

// Function call & Default display text
updateDisplay('Start typing...')

//  async functions
async function code() {
  const response = await fetch('snake.txt')
  const code = await response.text()
  return code
}

// Event listeners
async function typing() {
  const data = await code()
  let start = 0
  let stop = 2
  let text = ''
  
  document.addEventListener("keydown", (event) => {
    event.preventDefault()
    //  on each key down updateDisplay with data.slice(start, stop)
    text += data.slice(start, stop)
    updateDisplay(text)
    start += 2
    stop += 2
  })
}

typing();
