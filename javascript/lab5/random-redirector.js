/*
Create a page which randomly redirects to another. 
Create an array of urls (as strings), and randomly 
pick one using Math.random(). Then redirect to the 
page using window.location.

Using JavaScript's iframes, create a StumbleUpon clone. 
Embed the actual page you would redirect to in v1 and 
v2 in an iframe. Display different sites within the 
iframe when a button is clicked.
*/


// DOM Selectors:
const randomButton = document.querySelector('#rando')


// Variables:
const urls = [
  "https://www.bbc.com",
  "https://www.bbc.com/sport",
  "https://www.bbc.com/reel/",
  "http://www.bbc.com/travel/",
  "http://www.bbc.com/capital/",
  "https://www.bbc.com/sport/football",
  "https://www.bbc.com/sport/formula1",
  "https://www.bbc.com/sport/rugby-union",
  "https://www.bbc.com/sport/cycling",
]

// Functions:
const randomItem = (list) => {
  let randomIndex = Math.floor(Math.random() * list.length);
  return list[randomIndex];
}

// Version 1:
// const redirector = () => {
//  setTimeout(function() {
//      window.location.href = randomItem(urls)
//  }, 5000);
// }
// redirector()



// Version 2 event listener:
randomButton.addEventListener('click', (evt) => {
  document.getElementById('page').src = randomItem(urls);
  console.log(document.getElementById('page').src)
})

