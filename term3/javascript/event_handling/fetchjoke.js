function fetchJoke(){
    // Default method is "GET"
    fetch("https://icanhazdadjoke.com/", {
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(res => res.json())
    // .then(data => console.log(data))
}

// Adding .then here means we are obtaining the promise and customising the response
fetchJoke().then(joke => console.log(joke))
