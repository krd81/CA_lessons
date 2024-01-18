function challengeOne() {
    // const para = document.getElementById("output")
    const form = document.querySelector("form")

    form.addEventListener("submit", function(event) {
        event.preventDefault()
        let nameText = document.getElementById("name")
        let langText = document.getElementById("language")
        let cohortText = document.getElementById("cohort")
        let output = document.getElementById("output")

        output.textContent = `Hello ${nameText.value}, hope you are enjoying learning about 
        ${langText.value} in ${cohortText.value}`

        nameText.value = langText.value = cohortText.value = ""

    })

}

function challengeTwo() {
    const column = document.getElementById("challenge-two")
    const button = document.getElementById("change-theme")

    button.addEventListener("click", () => {
        let currentColour = window.getComputedStyle(column).getPropertyValue("background-color")

        if (currentColour === 'rgba(0, 0, 0, 0)') {
            column.classList.add("darkmode")
            button.textContent = "Light Mode"
        } else {
            column.classList.remove("darkmode")
            button.textContent = "Dark Mode"
        }
    })
}
/*
Drag events
Object: drag, dragstart, dragend
Target: dragover, dragenter, dragleave, drop
*/
function challengeThree() {
    const source = document.getElementById("dragger")

    let squares = document.getElementsByClassName("drag")

    for (let index in squares){
        squares[index].addEventListener("dragover", (event) => {
            event.preventDefault()}, false)


        squares[index].addEventListener("drop", (event) => {
            console.log(squares[index].id)
            event.preventDefault()
            squares[index].appendChild(source)
            
            if (squares[index].id === "to"){
                source.style.background = "rgb(24, 186, 100)"
            } else {
                source.style.background = "rgb(255, 0, 0)"
            }

        })

    }    
}

function challengeThreeSolution() {
    function drag(dragevent) {
        dragevent.dataTransfer.setData("text", dragevent.target.id);

    }

    function drop(dropevent) {
        dropevent.preventDefault();
        let data = dropevent.dataTransfer.getData("text");
        let child = document.getElementById(data)
        dropevent.target.appendChild(child)
        if (dropevent.target.id == "to") {
            child.style.backgroundColor = "green"
        } else {
            child.style.backgroundColor = "red"
        }
    }

    function allowDrop(allowdropevent) {
        allowdropevent.preventDefault();
    }

    let divs = document.getElementsByClassName("drag")
    for (let div of divs) {
        div.addEventListener('dragover', allowDrop)
        div.addEventListener('drop', drop)
        console.log(div)
    }

    document.getElementById("dragger").addEventListener('dragstart', drag)

}

function activity() {
    challengeOne()
    challengeTwo()
    challengeThreeSolution()
}

try {
    module.exports = {
        challengeOne,
        challengeTwo,
        challengeThree
    }
} catch {
}
