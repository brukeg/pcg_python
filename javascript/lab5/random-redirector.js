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


// Variables:
const urls = [
	"https://www.reddit.com/r/dankmemes/",
	"https://twitter.com/DankMemePlug",
	"https://www.facebook.com/PlaceForMemes",
	"https://www.tumblr.com/search/dank%20memes",
	"https://www.facebook.com/DankQualityMemes/",
	"https://browsedankmemes.com",
	"https://www.instagram.com/explore/tags/memesdaily/",
	"https://www.youtube.com/channel/UCAToczv95SVPQXYVycoqUKg",
	"https://dankmemeuniversity.tumblr.com",
]

// Functions:
const randomItem = (list) => {
  let randomIndex = Math.floor(Math.random() * list.length);
  return list[randomIndex];
}

const redirector = () => {
	setTimeout(function() {
  		window.location.href = randomItem(urls)
	}, 3000);
}

redirector()
