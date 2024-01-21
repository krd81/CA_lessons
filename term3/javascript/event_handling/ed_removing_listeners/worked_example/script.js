const balloon = document.getElementById("balloon")

// Returns the current size of the balloon
function getCurrentSize() {
    const currentSize = window.getComputedStyle(balloon).getPropertyValue("font-size")
    // Turn this into a number. It will be a string like "100px".
    return parseFloat(currentSize.slice(0,currentSize.indexOf("p")))
}

function handlePress(event) {
    const key = event.code
    console.log("key:", key)
    // If anything other than the enter or space key triggers
    // the event, just return
    if(key !== "Enter" && key !== "Space") 
        return

    // Either the enter or space key was hit - time for action!
    event.preventDefault()
    let currentSize = getCurrentSize()

    if(key === "Enter") {
        // Enter blows up the balloon        
        // if the size gets bigger than 200, blow up
        if(currentSize > 100) {
            balloon.textContent =  "💥"
            balloon.style.fontSize = "150px"
            window.removeEventListener("keypress", handlePress)
        }
        else {
            let sizeString = `${currentSize * 1.1}px`
            console.log("blowing up! to ", sizeString)
            balloon.style.fontSize = sizeString
        }
    }
    else {  // key is Space 
        // Space key deflates the balloon
        if(currentSize < 5) {
            balloon.textContent =  "🌈"
            balloon.style.fontSize = "100px"
            window.removeEventListener("keypress", handlePress)

        } else {
            let sizeString = `${currentSize *.9}px`
            console.log("deflating to ", sizeString)
            balloon.style.fontSize = sizeString    
        }
    }
}

window.addEventListener("keypress", handlePress)
