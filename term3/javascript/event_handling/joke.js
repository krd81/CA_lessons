// Updated the js file to use a promise instead of a callback function as in script.js

function getJoke() {
    return new Promise((resolve, reject) => {
        try{
            const req = new XMLHttpRequest()
            req.addEventListener('load', event => resolve(event.target.response.joke))

            req.open('GET', 'https://icanhazdadjoke.com/')
            req.setRequestHeader('Accept', 'application/json')
            req.responseType = 'json'
            req.send()
        }
        catch (e) {
            reject(e)
        }
    })
}

// getJoke().then(joke => console.log(joke))

const jokePromises = []
for (let i=0; i<3; i++){
    jokePromises.push(getJoke())
}

// console.log(jokePromises)
// 
Promise.all(jokePromises)
    .then(jokes => console.log(jokes))
    .catch(err => console.error(err))

console.log('Request sent!')