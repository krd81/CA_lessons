function challengeOne() {
    const btn5 = document.getElementById("five")
    const btn10 = document.getElementById("ten")
    const btn15 = document.getElementById("fifteen")
    const paraText = document.getElementById("counter-one")

    btn5.addEventListener("click", () => changeValue(5))
    btn10.addEventListener("click", () => changeValue(10))
    btn15.addEventListener("click", () => changeValue(15))

    getCurrentValue()
    function getCurrentValue() {        
        return parseInt(paraText.innerHTML)
    }


    function changeValue(value) {
        // This is the callback function for the event handler
        // It should increment the value in the <p> by value
        let currentValue = getCurrentValue()
        paraText.textContent = currentValue + value
    }
    // Challenge 1: Add an event listener to each button that invokes
    // the changeValue handler function with the correct value for the button
}

function challengeTwo() {
    const buttons = document.getElementsByClassName("challenge-two")
    const stopButton = document.getElementById("stop")
    const paraText = document.getElementById("counter-two")


    for (let button of buttons) {
        button.addEventListener("click", changeValue)
    }
    

    function changeValue(event) {
        // This is the callback function for the event handler
        // It should either increment the value, decrement the value,
        // or stop changing the value in the <p> based on the button that is clicked
        let currentValue = parseInt(paraText.innerHTML)
        let value = parseInt(event.target.value)
        paraText.textContent = currentValue + value
    }
    
    // Challenge 2: Use the event target to determine the value on the button
    // that triggered the click event. Add that value to the current value
    // in the paragraph and update what is shown on the page.
    // When the Stop button is clicked, the event handlers should all be removed.
    stopButton.addEventListener("click", () => {
        for (let button of buttons){
            button.removeEventListener("click", changeValue)
        }
    })

}


function activity() {
    challengeOne()
    challengeTwo()
}

try {
    module.exports = {
        challengeOne,
        challengeTwo
    }
} catch {
}
