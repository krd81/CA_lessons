// function adder(x, y, cb){
//     cb(x + y)
// }

// adder(5, 10, result => console.log(result))
// console.log("Done")

// const req = new XMLHttpRequest()
// req.addEventListener("load", event => {
//     const theJoke = JSON.parse(event.target.response)
//         console.log(theJoke)
//     })



// req.open("GET", "https://icanhazdadjoke.com/")
// req.setRequestHeader("Accept", "application/json")
// req.send()

// console.log("Request sent!")

function getJoke(cb){
    const req = new XMLHttpRequest()
    req.addEventListener("load", event => cb(event.target.response.joke))
    req.open("GET", "https://icanhazdadjoke.com/")
    req.setRequestHeader("Accept", "application/json")
    req.responseType = "json"
    req.send()
}

getJoke(joke => console.log(joke))

console.log("Request sent!")