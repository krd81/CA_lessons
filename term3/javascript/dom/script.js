
const items = [
    'Adding to the DOM',
    'Querying the DOM',
    'Changing the DOM',
    'Event Listeners'
]

const ul = document.querySelector('ul')


// Method 1:
for (let item of items){
    const newLi = document.createElement('li')
    newLi.innerText = item
    ul.appendChild(newLi)
}

// Method 2:
for (let item of items){
    ul.innerHTML += `<li>${item}</li>`
}


// Method 3:
const lis = items.map(item => `<li>${item}</li>`)
ul.innerHTML = lis.join('')

// Handle a mouse click onthe h1 element
// document.querySelector("h1").addEventListener("click", (event) => event.target.innerText += '!')

const newItem = document.querySelector("#newItem")
const btn = document.querySelector("button")

btn.addEventListener("click", () => {
    ul.innerHTML += `<li>${newItem.value}</li>`
    newItem.value = ""
})
