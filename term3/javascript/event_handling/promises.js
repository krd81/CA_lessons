const x = 2
const y = 5

function adder(a, b){
    return a + b
}

function adderPromise(x, y){
    // return new Promise((resolve, reject) => {      ** Alternative method **
    const calc = new Promise((resolve, reject) => {

        if (typeof x === "number" && typeof y === "number"){
            const answer = adder (x, y)        
            resolve(answer)                             
        } else {
            reject("x and y must be a number")
        }
    })
    return calc
}

// calc.then(value => console.log(value)).catch(err => console.error(err))
// calc
//     .then(value => console.log(value))
//     .catch(err => console.error(err))

adderPromise(10, 20)
    .then(value => console.log(value))
    .catch(err => console.error(err))

// adderPromise(3.7, 123.45)
    // .then(value => alert(value))
    // .catch(err => console.error(err))

// Nesting promises: Version 1
adderPromise(10, 20)
    .then(value => {
        adderPromise(value, 100)
        .then(value => console.log(value))
        
    })
    .catch(err => console.error(err))

// Nesting promises: Version 2
adderPromise(10, 20)
    // .then(value => {
    //     return adderPromise(value, 100)        
    // })
    .then(value => adderPromise(value, 100))
    .then(answer => console.log(answer))
    .catch(err => console.error(err))



console.log("Not waiting for resolve!")
