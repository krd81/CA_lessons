const age = 16

if (age >= 18) {
    console.log("Adult")
} else {
    console.log("Child")
}

/*
Python Ternary:
message = "Allowed" if age >= 18 else "Not Allowed"
*/

// JS Ternery
const message = age >=18 ? "Allowed" : "Not Allowed"

const favBird = "Pigeon"

switch (favBird) {
    case "Crow":
    case "Raven":        
        console.log("You like crows!")
        break
    case "Robin":
        console.log("You like robins!")
        break
    default:
        console.log("I don't know that bird!")
}
