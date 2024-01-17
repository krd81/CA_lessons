function challengeOne() {
/*
In the left most column, each time the button is clicked it should log 
"Hello World" to the console
*/
const btn = document.getElementById("challenge-one")

btn.addEventListener("click", () => console.log("Hello World"))
}

function challengeTwo() {
/*
In the middle column, there is an <ul>. 
Each time the button is pressed it should create an append a new <li>. 
Each list item will have the text "New List Item"
*/
const btn = document.getElementById("challenge-two")
let list = document.querySelector("ul")
btn.addEventListener("click", () => {
    let li = document.createElement("li")
    li.textContent = "New List Item"
    list.appendChild(li)
})

}


function challengeThree() {
/*
In the right most column which has an id of 'rainbow' and begins with a background colour of 
violet (rgb(238, 130, 238)). With each press of the button the background colour should cycle 
through each of the colours in the rainbow, these colours are in the array provided in the 
challengeThree function.

To properly achieve this, you will need to capture the current background colour, find that 
index in the array and set the new background colour to be the next position in the array.

Once the background colour gets the final position, red; the next button press will cycle back 
to the original violet colour.
*/
    const colours = ['rgb(238, 130, 238)', 'rgb(75, 0, 130)', 'rgb(0, 0, 255)', 'rgb(0, 128, 0)', 'rgb(255, 255, 0)', 'rgb(255, 165, 0)', 'rgb(255, 0, 0)']
    let div = document.getElementById("rainbow")
    let btn = document.getElementById("challenge-three")
    
    function getColourIndex(){
        let currentColour = window.getComputedStyle(div).getPropertyValue("background-color")

        for (let index in colours){
                if(colours[index] === currentColour){
                    return index
                }
        }        
    }

    btn.addEventListener("click", () => {
        let index
        if ((Number(getColourIndex()) + 1) === colours.length){
            index = 0
        } else {
            index = Number(getColourIndex()) + 1
        }
        div.style.backgroundColor = colours[index]
    })



}

function activity() {
    challengeOne()
    challengeTwo()
    challengeThree()
}

try {
    module.exports = {
        challengeOne,
        challengeTwo,
        challengeThree
    } 
} catch {
}
