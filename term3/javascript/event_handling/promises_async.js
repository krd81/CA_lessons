function adder(a, b){
    return a + b
}

async function adderPromise(x, y){
        if (typeof x === "number" && typeof y === "number"){
            const answer = adder (x, y)        
            return answer
        } else {
            throw "x and y must be a number"
        }
}

const value = await adderPromise(10, 20)
console.log(value)
    // .then(value => console.log(value))
    // .catch(err => console.error(err))

    console.log("Not waiting for resolve!")