const x = 2
const y = 5

function adder(a, b){
    return a + b
}

const calc = new Promise((resolve, reject) => {         
    if (typeof x === "number" && typeof y === "number"){
        const answer = adder (x, y)        
        resolve(answer)                             
    } else {
        reject("x and y must be a number")
    }
})

// calc.then(value => console.log(value)).catch(err => console.error(err))
calc
    .then(value => console.log(value))
    .catch(err => console.error(err))


console.log("Not waiting for resolve!")
console.log(calc)