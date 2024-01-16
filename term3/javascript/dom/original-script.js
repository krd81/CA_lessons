// const el = document.getElementById("foo")  << pre ES6 method to create object
const el = document.querySelectorAll("li")
console.log(el)
// el.innerHTML= 'Hello <span style="color: red"> World!</span>'

const newDiv = document.createElement("div")
// document.body.appendChild(newDiv) Adds to end
// document.querySelector("ul").appendChild(newDiv)
document.body.insertBefore(newDiv, document.querySelector("ul"))
newDiv.innerHTML = "<h3>Awesome content!</h3>"
newDiv.style.color = "violet"
console.log(newDiv)

const myColor = "blue"
document.body.innerHTML += `<div id="spam" style="color: ${myColor}"><h3>Awesome content!</h3></div>`
