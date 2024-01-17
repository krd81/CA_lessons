function getJoke(cb) {
    // 2. Create XHR
    const req = new XMLHttpRequest()
    // 3. Add listener for when the response is received and parsed
    // 9. Listener callback is triggered, which in turn calls cb, passing the joke
    req.addEventListener('load', event => cb(event.target.response.joke))
    req.addEventListener('',)
    // 4. Open the URL with the appropriate verb
    req.open('GET', 'https://icanhazdadjoke.com/')
    // 5. Set Accept header so server gives us JSON
    req.setRequestHeader('Accept', 'application/json')
    // 6. Set responeType so XHR object parses the JSON
    req.responseType = 'json'
    // 7. Send the request, then immediately return from getJoke (i.e. don't wait!)
    req.send()
}

// 1. Call getJoke and pass a callback function
// 10. Callback is called via cb in the load listener in getJoke, receiving the joke
getJoke(joke => console.log(joke))

// 8. getJoke returned immediately, so log out message
console.log('Request sent!')



/*
Convert arrow function to normal function:
event => cb(event.target.response.joke)

function callback (event){
    return event.target.response.joke
}


joke => console.log(joke)

function printJoke(joke){
    console.log(joke)
}


*/